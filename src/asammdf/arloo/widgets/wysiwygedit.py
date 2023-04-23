from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from . import toolbar_resource

import os
import uuid

FONT_SIZES = [7, 8, 9, 10, 11, 12, 13, 14, 18, 24, 36, 48, 64, 72, 96, 144, 288]
IMAGE_EXTENSIONS = ['.jpg', '.png']
HTML_EXTENSIONS = ['.htm', '.html']


def hexuuid():
    return uuid.uuid4().hex


def splitext(p):
    return os.path.splitext(p)[1].lower()


class TextEdit(QTextEdit):

    def canInsertFromMimeData(self, source):

        if source.hasImage():
            return True
        else:
            return super(TextEdit, self).canInsertFromMimeData(source)

    def insertFromMimeData(self, source):

        cursor = self.textCursor()
        document = self.document()

        if source.hasUrls():

            for u in source.urls():
                file_ext = splitext(str(u.toLocalFile()))
                if u.isLocalFile() and file_ext in IMAGE_EXTENSIONS:
                    image = QImage(u.toLocalFile())
                    document.addResource(QTextDocument.ImageResource, u, image)
                    cursor.insertImage(u.toLocalFile())

                else:
                    # If we hit a non-image or non-local URL break the loop and fall out
                    # to the super call & let Qt handle it
                    break

            else:
                # If all were valid images, finish here.
                return


        elif source.hasImage():
            image = source.imageData()
            uuid = hexuuid()
            document.addResource(QTextDocument.ImageResource, uuid, image)
            cursor.insertImage(uuid)
            return

        super(TextEdit, self).insertFromMimeData(source)


class WysiwygEdit(QWidget):

    def __init__(self, *args, **kwargs):
        super(WysiwygEdit, self).__init__(*args, **kwargs)

        layout = QVBoxLayout(self)
        self.editor = TextEdit()
        # Setup the QTextEdit editor configuration
        self.editor.setAutoFormatting(QTextEdit.AutoAll)
        self.editor.selectionChanged.connect(self.update_format)
        # Initialize default font size.
        font = QFont('Times', 12)
        self.editor.setFont(font)
        # We need to repeat the size to init the current format.
        self.editor.setFontPointSize(12)

        # self.path holds the path of the currently open file.
        # If none, we haven't got a file open yet (or creating new).
        self.path = None

        toolbar_layout = QHBoxLayout()
        layout.addLayout(toolbar_layout)
        edit_toolbar = QToolBar("Edit")
        edit_toolbar.setIconSize(QSize(16, 16))
        toolbar_layout.addWidget(edit_toolbar)

        undo_action = QAction(QIcon(":/arrow-curve-180-left.png"), "Undo", self)
        undo_action.setStatusTip("Undo last change")
        undo_action.triggered.connect(self.editor.undo)

        redo_action = QAction(QIcon(":/arrow-curve.png"), "Redo", self)
        redo_action.setStatusTip("Redo last change")
        redo_action.triggered.connect(self.editor.redo)
        edit_toolbar.addAction(redo_action)


        cut_action = QAction(QIcon(":/scissors.png"), "Cut", self)
        cut_action.setStatusTip("Cut selected text")
        cut_action.setShortcut(QKeySequence.Cut)
        cut_action.triggered.connect(self.editor.cut)
        edit_toolbar.addAction(cut_action)

        copy_action = QAction(QIcon(":/document-copy.png"), "Copy", self)
        copy_action.setStatusTip("Copy selected text")
        cut_action.setShortcut(QKeySequence.Copy)
        copy_action.triggered.connect(self.editor.copy)
        edit_toolbar.addAction(copy_action)

        paste_action = QAction(QIcon(":/clipboard-paste-document-text.png"), "Paste", self)
        paste_action.setStatusTip("Paste from clipboard")
        cut_action.setShortcut(QKeySequence.Paste)
        paste_action.triggered.connect(self.editor.paste)
        edit_toolbar.addAction(paste_action)

        select_action = QAction(QIcon(":/selection-input.png"), "Select all", self)
        select_action.setStatusTip("Select all text")
        cut_action.setShortcut(QKeySequence.SelectAll)
        select_action.triggered.connect(self.editor.selectAll)


        wrap_action = QAction(QIcon(":/arrow-continue.png"), "Wrap text to window", self)
        wrap_action.setStatusTip("Toggle wrap text to window")
        wrap_action.setCheckable(True)
        wrap_action.setChecked(True)
        wrap_action.triggered.connect(self.edit_toggle_wrap)

        format_toolbar = QToolBar("Format")
        format_toolbar.setIconSize(QSize(16, 16))
        toolbar_layout.addWidget(format_toolbar)

        # We need references to these actions/settings to update as selection changes, so attach to self.
        self.fonts = QFontComboBox()
        self.fonts.currentFontChanged.connect(self.editor.setCurrentFont)
        format_toolbar.addWidget(self.fonts)

        self.fontsize = QComboBox()
        self.fontsize.addItems([str(s) for s in FONT_SIZES])

        # Connect to the signal producing the text of the current selection. Convert the string to float
        # and set as the pointsize. We could also use the index + retrieve from FONT_SIZES.
        self.fontsize.currentIndexChanged.connect(self.change_fontsize)
        format_toolbar.addWidget(self.fontsize)

        self.bold_action = QAction(QIcon(":/edit-bold.png"), "볼드체", self)
        self.bold_action.setStatusTip("볼드체")
        self.bold_action.setShortcut(QKeySequence.Bold)
        self.bold_action.setCheckable(True)
        self.bold_action.toggled.connect(self.toggle_boldface)
        format_toolbar.addAction(self.bold_action)

        self.italic_action = QAction(QIcon(":/edit-italic.png"), "이탤릭", self)
        self.italic_action.setStatusTip("이탤릭")
        self.italic_action.setShortcut(QKeySequence.Italic)
        self.italic_action.setCheckable(True)
        self.italic_action.toggled.connect(self.editor.setFontItalic)
        format_toolbar.addAction(self.italic_action)

        self.underline_action = QAction(QIcon(":/edit-underline.png"), "밑줄", self)
        self.underline_action.setStatusTip("밑줄")
        self.underline_action.setShortcut(QKeySequence.Underline)
        self.underline_action.setCheckable(True)
        self.underline_action.toggled.connect(self.editor.setFontUnderline)
        format_toolbar.addAction(self.underline_action)


        self.alignl_action = QAction(QIcon(":/edit-alignment.png"), "왼쪽 정렬", self)
        self.alignl_action.setStatusTip("왼쪽 정렬")
        self.alignl_action.setCheckable(True)
        self.alignl_action.triggered.connect(lambda: self.editor.setAlignment(Qt.AlignLeft))
        format_toolbar.addAction(self.alignl_action)

        self.alignc_action = QAction(QIcon(":/edit-alignment-center.png"), "중앙 정렬", self)
        self.alignc_action.setStatusTip("중앙 정렬")
        self.alignc_action.setCheckable(True)
        self.alignc_action.triggered.connect(lambda: self.editor.setAlignment(Qt.AlignCenter))
        format_toolbar.addAction(self.alignc_action)

        self.alignr_action = QAction(QIcon(":/edit-alignment-right.png"), "오른쪽 정렬", self)
        self.alignr_action.setStatusTip("오른쪽 정렬")
        self.alignr_action.setCheckable(True)
        self.alignr_action.triggered.connect(lambda: self.editor.setAlignment(Qt.AlignRight))
        format_toolbar.addAction(self.alignr_action)

        self.alignj_action = QAction(QIcon(":/edit-alignment-justify.png"), "좌우폭 채움", self)
        self.alignj_action.setStatusTip("좌우폭 채움")
        self.alignj_action.setCheckable(True)
        self.alignj_action.triggered.connect(lambda: self.editor.setAlignment(Qt.AlignJustify))
        format_toolbar.addAction(self.alignj_action)

        format_group = QActionGroup(self)
        format_group.setExclusive(True)
        format_group.addAction(self.alignl_action)
        format_group.addAction(self.alignc_action)
        format_group.addAction(self.alignr_action)
        format_group.addAction(self.alignj_action)

        # A list of all format-related widgets/actions, so we can disable/enable signals when updating.
        self._format_actions = [
            self.fonts,
            self.fontsize,
            self.bold_action,
            self.italic_action,
            self.underline_action,
            # We don't need to disable signals for alignment, as they are paragraph-wide.
        ]

        layout.addWidget(self.editor)

        # Initialize.
        self.update_format()
        self.show()

    def change_fontsize(self, index):
        text = self.fontsize.itemText(index)
        return self.editor.setFontPointSize(float(text))

    def toggle_boldface(self, x):
        return self.editor.setFontWeight(QFont.Bold if x else QFont.Normal)

    def block_signals(self, objects, b):
        for o in objects:
            o.blockSignals(b)

    def update_format(self):
        """
        Update the font format toolbar/actions when a new text selection is made. This is neccessary to keep
        toolbars/etc. in sync with the current edit state.
        :return:
        """
        # Disable signals for all format widgets, so changing values here does not trigger further formatting.
        self.block_signals(self._format_actions, True)

        self.fonts.setCurrentFont(self.editor.currentFont())
        # Nasty, but we get the font-size as a float but want it was an int
        self.fontsize.setCurrentText(str(int(self.editor.fontPointSize())))

        self.italic_action.setChecked(self.editor.fontItalic())
        self.underline_action.setChecked(self.editor.fontUnderline())
        self.bold_action.setChecked(self.editor.fontWeight() == QFont.Bold)

        self.alignl_action.setChecked(self.editor.alignment() == Qt.AlignLeft)
        self.alignc_action.setChecked(self.editor.alignment() == Qt.AlignCenter)
        self.alignr_action.setChecked(self.editor.alignment() == Qt.AlignRight)
        self.alignj_action.setChecked(self.editor.alignment() == Qt.AlignJustify)

        self.block_signals(self._format_actions, False)

    def dialog_critical(self, s):
        dlg = QMessageBox(self)
        dlg.setText(s)
        dlg.setIcon(QMessageBox.Critical)
        dlg.show()

    def edit_toggle_wrap(self):
        self.editor.setLineWrapMode(1 if self.editor.lineWrapMode() == 0 else 0)
