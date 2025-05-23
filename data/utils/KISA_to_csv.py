import csv
import os
import pandas as pd

PATH = "./data/KISA/raw"
SAVE_PATH = "./data/KISA/csv/"

def csv_to_list(file_name):
    question_list = []
    f = open(file_name, 'r', encoding='utf-8')
    rdr = csv.reader(f)
    index = 1
    for line in rdr:
        question_text = ''
        if line == []:
            continue
        elif line[0] == 'SMS/-[(KISA:EOL)]':
            continue
        else:
            text = line[0].split('[(KISA)]')
            for i in range(len(text)):
                if i ==3:
                    question_text += text[i]
                    question_list.append([1,question_text])
                    index += 1
    
    return question_list

dir_list = os.listdir(PATH)
for item in dir_list:
    SAVE_PATH = "./data/KISA/csv/"
    file_path = PATH + "/" + item
    spams = csv_to_list(file_path)
    SAVE_PATH = SAVE_PATH + item[:-4]+".csv"
    df = pd.DataFrame(spams)
    df.to_csv(SAVE_PATH, header=None, encoding='utf-8-sig')
    print("Finished writing file ", SAVE_PATH)
    print(len(spams))