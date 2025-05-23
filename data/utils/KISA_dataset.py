# dataset_갯수.txt에 따라서 진행함
# 5514 ./data/KISA/csv/20231126_GBL.csv  -> 2000
# 5803 ./data/KISA/csv/20231203_GBL.csv  -> 2000
# 6961 ./data/KISA/csv/20231210_GBL.csv  -> 2000
# 6038 ./data/KISA/csv/20231217_GBL.csv  -> 2000
# 8901 ./data/KISA/csv/20231224_GBL.csv  -> 2000

import csv
import os
import random
import pandas as pd

PATH = "./data/KISA/csv"
SAVE_PATH = "./data/KISA/preprocessed/"

dir_list = os.listdir(PATH)

for item in dir_list:
    if item != "20231126_GBL.csv": # json 파일별로 이름을 돌리면서 직접 csv 파일 생성함
        continue
    file_path = PATH + "/" + item
    print(file_path)
    data = pd.read_csv(file_path, header=None)
    df_to_list = data.values.tolist()
    choice_df = random.sample(df_to_list, 2000)
    choice_df.sort(key=lambda x:x[0])
    df = pd.DataFrame(choice_df)
    df.drop([0], axis=1, inplace=True)
    print(df)
        
    SAVE_PATH = SAVE_PATH + item[:-4] + "_2000"+ ".csv"

df.to_csv(SAVE_PATH, header=None, index=None, encoding='utf-8-sig')
print("Finished writing file ", SAVE_PATH)
print(len(df))
