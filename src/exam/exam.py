from pathlib import Path

from PySide6.QtCore import QResource, QFile, QTextStream, QStringDecoder, QIODevice
from canmatrix import canmatrix

from asammdf import MDF, Signal
import sys
import pandas as pd
import numpy as np
from asammdf.gui.arloo import arresource_rc


# import matplotlib.pyplot as plt

def read_and_plot(input_filename):
    # MDF 파일을 읽어옵니다.
    # path = "MDF 파일을 저장한 경로"
    raw_data = MDF(input_filename)
    databases = {
        "CAN": [("logfile/280-V00-BRA-030902-database.dbc", 0)],
    }
    data = raw_data.extract_bus_logging(database_files=databases)
    print("start time is {}".format(data.start_time))

    ### CAN 신호 리스트를 가져 옵니다.
    signal_list = list(data.channels_db)
    print("{0} ... (and {1} more)".format(signal_list[:5],len(signal_list)-5))  # 로깅된 CAN 신호 전체를 볼 수 있습니다.
    # 가져온 리스트에서 시간축은 신호가 아니므로 제외합니다.
    # signal_list.remove('Timestamp')
    # print(signal_list)  # 로깅된 CAN 신호 전체를 볼 수 있습니다.

    ### 그래프 출력
    speed = data.get(signal_list[7])
    speed.plot()
    # speed = data.get(signal_list[8])
    # speed.plot
    filtered_signal_list = []
    ### 여러 그래프 출력
    # for signal in data.select(filtered_signal_list):
    #     signal.plot()

    ### 필요한 신호만 필터링
    filtered_signal_list = ['CAN_DataFrame', 'CAN_DataFrame.BusChannel', 'CAN_DataFrame.ID', 'CAN_DataFrame.IDE']
    # 10초 ~ 12초 사이의 데이터만 필터링
    #    filtered_data = data.filter(filtered_signal_list) # .cut(start=10, stop=12)

    ### 엑셀 파일 또는 CSV 파일로 출력
    signals_data_frame = data.to_dataframe()
    # signals_data_frame.to_excel(path + "signals_data_frame.xlsx")
    fileName = Path(input_filename).stem
    output_filename = fileName + "signals_data_frame.csv"
    signals_data_frame.to_csv(Path(input_filename).parent.joinpath(output_filename))
    exit()


if __name__ == "__main__":
    argLen = len(sys.argv)
    if argLen < 2:
        print("filename is required")
        exit(1)
    intput_file_name = sys.argv[1]
    read_and_plot(intput_file_name)
