from __future__ import annotations

import csv
import logging
from pathlib import Path

from typing_extensions import Literal

from asammdf import MDF
from asammdf.arloo.arloos import DEFAULT_TIME_ZONE
from asammdf.blocks.utils import UniqueDB, TERMINATED, csv_int2hex, csv_bytearray2hex
from asammdf.mdf import LOCAL_TIMEZONE
from asammdf.types import StrPathType
import pandas as pd

logger = logging.getLogger("mdf.export.csv")


class MDFCsvExporter:
    def export(
        self,
        mdf: MDF,
        filename: StrPathType | None = None,
        progress=None,
        **kwargs,
    ) -> None:
        r"""(copied from original *MDF* implementation. csv전용)
        export *MDF* to other formats. The *MDF* file name is used is
        available, else the *filename* argument must be provided.

        The *pandas* export option was removed. you should use the method
        *to_dataframe* instead.

        Parameters
        ----------
        fmt : string
            can be one of the following:

            * `csv` : CSV export that uses the "," delimiter. This option
              will generate a new csv file for each data group
              (<MDFNAME>_DataGroup_<cntr>.csv)

            * `hdf5` : HDF5 file output; each *MDF* data group is mapped to
              a *HDF5* group with the name 'DataGroup_<cntr>'
              (where <cntr> is the index)

            * `mat` : Matlab .mat version 4, 5 or 7.3 export. If
              *single_time_base==False* the channels will be renamed in the mat
              file to 'D<cntr>_<channel name>'. The channel group
              master will be renamed to 'DM<cntr>_<channel name>'
              ( *<cntr>* is the data group index starting from 0)

            * `parquet` : export to Apache parquet format

        filename : string | pathlib.Path
            export file name

        \*\*kwargs

            * `single_time_base`: resample all channels to common time base,
              default *False*
            * `raster`: float time raster for resampling. Valid if
              *single_time_base* is *True*
            * `time_from_zero`: adjust time channel to start from 0
            * `use_display_names`: use display name instead of standard channel
              name, if available.
            * `empty_channels`: behaviour for channels without samples; the
              options are *skip* or *zeros*; default is *skip*
            * `format`: only valid for *mat* export; can be '4', '5' or '7.3',
              default is '5'
            * `oned_as`: only valid for *mat* export; can be 'row' or 'column'
            * `keep_arrays` : keep arrays and structure channels as well as the
              component channels. If *True* this can be very slow. If *False*
              only the component channels are saved, and their names will be
              prefixed with the parent channel.
            * `reduce_memory_usage` : bool
              reduce memory usage by converting all float columns to float32 and
              searching for minimum dtype that can reprezent the values found
              in integer columns; default *False*
            * `compression` : str
              compression to be used

              * for ``parquet`` : "GZIP" or "SNAPPY"
              * for ``hfd5`` : "gzip", "lzf" or "szip"
              * for ``mat`` : bool

            * `time_as_date` (False) : bool
              export time as local timezone datetimee; only valid for CSV export

              .. versionadded:: 5.8.0

            * `ignore_value2text_conversions` (False) : bool
              valid only for the channels that have value to text conversions and
              if *raw=False*. If this is True then the raw numeric values will be
              used, and the conversion will not be applied.

              .. versionadded:: 5.8.0

            * raw (False) : bool
              export all channels using the raw values

              .. versionadded:: 6.0.0

            * delimiter (',') : str
              only valid for CSV: see cpython documentation for csv.Dialect.delimiter

              .. versionadded:: 6.2.0

            * doublequote (True) : bool
              only valid for CSV: see cpython documentation for csv.Dialect.doublequote

              .. versionadded:: 6.2.0

            * escapechar (None) : str
              only valid for CSV: see cpython documentation for csv.Dialect.escapechar

              .. versionadded:: 6.2.0

            * lineterminator ("\\r\\n") : str
              only valid for CSV: see cpython documentation for csv.Dialect.lineterminator

              .. versionadded:: 6.2.0

            * quotechar ('"') : str
              only valid for CSV: see cpython documentation for csv.Dialect.quotechar

              .. versionadded:: 6.2.0

            * quoting ("MINIMAL") : str
              only valid for CSV: see cpython documentation for csv.Dialect.quoting. Use the
              last part of the quoting constant name

              .. versionadded:: 6.2.0

            * add_units (False) : bool
              only valid for CSV: add the channel units on the second row of the CSV file

              .. versionadded:: 7.1.0
              :param mdf:


        """

        header_items = (
            "date",
            "time",
            "author_field",
            "department_field",
            "project_field",
            "subject_field",
        )

        single_time_base = kwargs.get("single_time_base", False)
        raster = kwargs.get("raster", None)
        time_from_zero = kwargs.get("time_from_zero", True)
        channel_names_dict = kwargs.get("channel_names", [])
        use_display_names = kwargs.get("use_display_names", True)
        empty_channels = kwargs.get("empty_channels", "skip")
        format = kwargs.get("format", "5")
        oned_as = kwargs.get("oned_as", "row")
        reduce_memory_usage = kwargs.get("reduce_memory_usage", False)
        compression = kwargs.get("compression", "")
        time_as_date = kwargs.get("time_as_date", False)
        ignore_value2text_conversions = kwargs.get(
            "ignore_value2text_conversions", False
        )
        raw = bool(kwargs.get("raw", False))

        if compression == "SNAPPY":
            try:
                import snappy
            except ImportError:
                logger.warning(
                    "snappy compressor is not installed; compression will be set to GZIP"
                )
                compression = "GZIP"

        filename = Path(filename) if filename else mdf.name

        if single_time_base:
            df = mdf.to_dataframe(
                raster=raster,
                time_from_zero=time_from_zero,
                use_display_names=use_display_names,
                empty_channels=empty_channels,
                reduce_memory_usage=reduce_memory_usage,
                ignore_value2text_conversions=ignore_value2text_conversions,
                raw=raw,
                numeric_1D_only=False,
            )
            units = {}
            comments = {}
            used_names = UniqueDB()

            groups_nr = len(mdf.groups)
            if progress is not None:
                if callable(progress):
                    progress(0, groups_nr * 2)
                else:
                    progress.signals.setMaximum.emit(groups_nr * 2)

                    if progress.stop:
                        return TERMINATED

            for i, grp in enumerate(mdf.groups):
                if progress is not None and progress.stop:
                    return TERMINATED

                for ch in grp.channels:
                    if use_display_names:
                        channel_name = (
                            list(ch.display_names)[0] if ch.display_names else ch.name
                        )
                    else:
                        channel_name = ch.name

                    channel_name = used_names.get_unique_name(channel_name)

                    if hasattr(ch, "unit"):
                        unit = ch.unit
                        if ch.conversion:
                            unit = unit or ch.conversion.unit
                    else:
                        unit = ""
                    comment = ch.comment

                    units[channel_name] = unit
                    comments[channel_name] = comment

                if progress is not None:
                    if callable(progress):
                        progress(i + 1, groups_nr * 2)
                    else:
                        progress.signals.setValue.emit(i + 1)

                        if progress.stop:
                            return TERMINATED

        fmtparams = {
            "delimiter": kwargs.get("delimiter", ",")[0],
            "doublequote": kwargs.get("doublequote", True),
            "lineterminator": kwargs.get("lineterminator", "\r\n"),
            "quotechar": kwargs.get("quotechar", '"')[0],
        }

        quoting = kwargs.get("quoting", "MINIMAL").upper()
        quoting = getattr(csv, f"QUOTE_{quoting}")

        fmtparams["quoting"] = quoting

        escapechar = kwargs.get("escapechar", '"')
        if escapechar is not None:
            escapechar = escapechar[0]

        fmtparams["escapechar"] = escapechar

        if single_time_base:
            filename = filename.with_suffix(".csv")
            message = f'Writing csv export to file "{filename}"'
            logger.info(message)

            if time_as_date:
                index = (
                    pd.to_datetime(
                        df.index + mdf.header.start_time.timestamp(), unit="s"
                    )
                    .tz_localize("UTC")
                    .tz_convert(DEFAULT_TIME_ZONE)
                    .astype(str)
                )
                df.index = index
                df.index.name = "timestamps"

                units["timestamps"] = ""
            else:
                units["timestamps"] = "s"

            if hasattr(self, "can_logging_db") and mdf.can_logging_db:
                dropped = {}

                for name_ in df.columns:
                    if name_.endswith("CAN_DataFrame.ID"):
                        dropped[name_] = pd.Series(
                            csv_int2hex(df[name_].astype("<u4") & 0x1FFFFFFF),
                            index=df.index,
                        )

                    elif name_.endswith("CAN_DataFrame.DataBytes"):
                        dropped[name_] = pd.Series(
                            csv_bytearray2hex(df[name_]), index=df.index
                        )

                df = df.drop(columns=list(dropped))
                for name, s in dropped.items():
                    df[name] = s

            with open(filename, "w", newline="") as csvfile:
                writer = csv.writer(csvfile, **fmtparams)

                names_row = [df.index.name, *df.columns]
                writer.writerow(names_row)

                if kwargs.get("add_units", False):
                    units_row = [units[name] for name in names_row]
                    writer.writerow(units_row)

                for col in df:
                    if df[col].dtype.kind == "S":
                        for encoding, errors in (
                            ("utf-8", "strict"),
                            ("latin-1", "strict"),
                            ("utf-8", "replace"),
                            ("latin-1", "replace"),
                        ):
                            try:
                                df[col] = df[col] = df[col].str.decode(
                                    encoding, errors
                                )
                                break
                            except:
                                continue

                if reduce_memory_usage:
                    vals = [df.index, *(df[name] for name in df)]
                else:
                    vals = [
                        df.index.to_list(),
                        *(df[name].to_list() for name in df),
                    ]
                count = len(df.index)

                if progress is not None:
                    if callable(progress):
                        progress(0, count)
                    else:
                        progress.signals.setValue.emit(0)
                        progress.signals.setMaximum.emit(count)

                        if progress.stop:
                            return TERMINATED

                for i, row in enumerate(zip(*vals)):
                    writer.writerow(row)

                    if progress is not None:
                        if callable(progress):
                            progress(i + 1, count)
                        else:
                            progress.signals.setValue.emit(i + 1)
                            if progress.stop:
                                return TERMINATED

        else:
            add_units = kwargs.get("add_units", False)

            filename = filename.with_suffix(".csv")

            gp_count = len(mdf.virtual_groups)

            if progress is not None:
                if callable(progress):
                    progress(0, gp_count)
                else:
                    progress.signals.setValue.emit(0)
                    progress.signals.setMaximum.emit(gp_count)

                    if progress.stop:
                        return TERMINATED

            for i, (group_index, virtual_group) in enumerate(
                mdf.virtual_groups.items()
            ):
                if progress is not None and progress.stop:
                    return TERMINATED

                message = f"Exporting group {i+1} of {gp_count}"
                logger.info(message)

                if len(virtual_group.groups) == 1:
                    comment = mdf.groups[
                        virtual_group.groups[0]
                    ].channel_group.comment
                else:
                    comment = ""

                if comment:
                    for char in f'\n\t\r\b <>\/:"?*|':
                        comment = comment.replace(char, "_")
                    group_csv_name = (
                        filename.parent
                        / f"{filename.stem}.ChannelGroup_{i}_{comment}.csv"
                    )
                else:
                    group_csv_name = (
                        filename.parent / f"{filename.stem}.ChannelGroup_{i}.csv"
                    )

                df = mdf.get_group(
                    group_index,
                    raster=raster,
                    time_from_zero=time_from_zero,
                    use_display_names=use_display_names,
                    reduce_memory_usage=reduce_memory_usage,
                    ignore_value2text_conversions=ignore_value2text_conversions,
                    raw=raw,
                )

                if add_units:
                    units = {}
                    used_names = UniqueDB()

                    for gp_index, channel_indexes in mdf.included_channels(
                        group_index
                    )[group_index].items():
                        for ch_index in channel_indexes:
                            ch = mdf.groups[gp_index].channels[ch_index]

                            if use_display_names:
                                channel_name = (
                                    list(ch.display_names)[0]
                                    if ch.display_names
                                    else ch.name
                                )
                            else:
                                channel_name = ch.name

                            channel_name = used_names.get_unique_name(channel_name)

                            if hasattr(ch, "unit"):
                                unit = ch.unit
                                if ch.conversion:
                                    unit = unit or ch.conversion.unit
                            else:
                                unit = ""

                            units[channel_name] = unit
                else:
                    units = {}

                if time_as_date:
                    index = (
                        pd.to_datetime(
                            df.index + mdf.header.start_time.timestamp(), unit="s"
                        )
                        .tz_localize("UTC")
                        .tz_convert(LOCAL_TIMEZONE)
                        .astype(str)
                    )
                    df.index = index
                    df.index.name = "timestamps"

                    units["timestamps"] = ""
                else:
                    units["timestamps"] = "s"

                with open(group_csv_name, "w", newline="") as csvfile:
                    writer = csv.writer(csvfile, **fmtparams)

                    if hasattr(self, "can_logging_db") and mdf.can_logging_db:
                        dropped = {}

                        for name_ in df.columns:
                            if name_.endswith("CAN_DataFrame.ID"):
                                dropped[name_] = pd.Series(
                                    csv_int2hex(df[name_] & 0x1FFFFFFF),
                                    index=df.index,
                                )

                            elif name_.endswith("CAN_DataFrame.DataBytes"):
                                dropped[name_] = pd.Series(
                                    csv_bytearray2hex(df[name_]), index=df.index
                                )

                        df = df.drop(columns=list(dropped))
                        for name_, s in dropped.items():
                            df[name_] = s

                    # csv 헤더는 고객이 설정한 이름으로 세팅
                    names_row = [df.index.name]
                    for col in df.columns:
                        if col in channel_names_dict:
                            names_row.append(channel_names_dict[col])
                        else:
                            names_row.append(col)
                    writer.writerow(names_row)

                    if add_units:
                        units_row = [units[name] for name in names_row]
                        writer.writerow(units_row)

                    if reduce_memory_usage:
                        vals = [df.index, *(df[name] for name in df)]
                    else:
                        vals = [
                            df.index.to_list(),
                            *(df[name].to_list() for name in df),
                        ]

                    for i, row in enumerate(zip(*vals)):
                        writer.writerow(row)

                if progress is not None:
                    if callable(progress):
                        progress(i + 1, gp_count)
                    else:
                        progress.signals.setValue.emit(i + 1)

                        if progress.stop:
                            return TERMINATED
