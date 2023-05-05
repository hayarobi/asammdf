import logging
from math import inf
from pathlib import Path

from numpy import inf
from typing_extensions import Literal

from asammdf import MDF
from asammdf.gui.utils import TERMINATED
from asammdf.mdf_csv_export import MDFCsvExporter
from asammdf.types import StrPathType

logger = logging.getLogger("arloo.exporter")


class ExportOption(object):
    def __init__(self) -> None:
        super().__init__()
        self.export_dir = 'export'
        self.file_prefix = 'export-'
        self.filter_channel = False
        self.channels = []
        self.start_offset = -1
        self.end_offset = inf
        self.use_display_names = False
        self.time_as_date = True

    def is_cut(self):
        return self.start_offset > 0 or self.end_offset < inf


class CsvExporter(object):
    def __init__(self, mdf: MDF) -> None:
        super().__init__()
        self.doublequote = None
        self.mdf = mdf

    def exportToFile(self, opts: ExportOption):
        split_size = 0
        self.mdf.configure(read_fragment_size=split_size)

        mdf = self.mdf

        if opts.filter_channel:
            channel_names = {}
            filter_channels = []
            for sig in opts.channels:
                channel_names[sig.original_name] = sig.name
                filter_channels.append((None, sig.group_index, sig.channel_index))
            logger.debug(f"filter channels {opts.channels}")

            result = self.mdf.filter(
                channels=filter_channels,
            )
            if result is TERMINATED:
                return
            else:
                mdf = result
            mdf.configure(
                read_fragment_size=split_size,
                write_fragment_size=split_size,
            )

        if opts.is_cut():
            logger.debug(f"limit range from {opts.start_offset} to {opts.end_offset}")

            # cut self.mdf
            result = mdf.cut(
                start=opts.start_offset,
                stop=opts.end_offset,
                version="4.10",
                time_from_zero=False,
                include_ends=False,
            )

            if result is TERMINATED:
                return
            else:
                mdf.close()
                mdf = result

            mdf.configure(
                read_fragment_size=split_size,
                write_fragment_size=split_size,
            )

        delimiter = ","
        double_quote = True
        escape_char = None
        quote_char = '"'

        export_dir = Path(opts.export_dir)
        if not export_dir.exists():
            export_dir.mkdir()
        kwargs = {
            "fmt": "csv",
            "filename": export_dir.joinpath(opts.file_prefix),
            # "single_time_base": False,
            "channel_names": channel_names,
            "use_display_names": opts.use_display_names,
            "time_as_date": opts.time_as_date,
            "format": "csv",
            "raster": None,
            "delimiter": delimiter,
            "doublequote": double_quote,
            "escapechar": escape_char,
            "quotechar": quote_char,
        }

        mdf_exporter = MDFCsvExporter()
        mdf_exporter.export(mdf, **kwargs)
