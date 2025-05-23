# 해당 파일은 csv 파일을 엑셀 파일로 변환해주는 파일입니다.

import pandas as pd
import csv

# 답변을 계속해서 append 해주는 방식
def make_csv(csv_path, index, data):
    if index == 0:
        f = open(csv_path, 'w', encoding='utf-8-sig', newline='')
    else:
        f = open(csv_path, 'a', encoding='utf-8-sig', newline='')
    wr = csv.writer(f)
    # 리스트 형식의 데이터가 있는 경우 루프를 돌려서 입력 가능
    #for data in response_list:
    wr.writerow(data)
    f.close()

def make_excel(csv_path, file_name):
    csv_name = csv_path[:-4]
    read_file = pd.read_csv (csv_name+'.csv')
    read_file.to_excel (csv_name+'.xlsx', index = True, header=False)
    return