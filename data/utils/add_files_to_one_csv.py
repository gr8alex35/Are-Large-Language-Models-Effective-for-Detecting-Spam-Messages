import os
import pandas as pd

# KISA Path
PATH = "./data/KISA/preprocessed"
SAVE_PATH = "./data/KISA/preprocessed/KISA_SPAM.csv"

# # AIHUB Path
# PATH = "./data/한국어_SNS/csv"
# SAVE_PATH = "./data/한국어_SNS/preprocessed/AIHUB_NONSPAM.csv"

dir_list = os.listdir(PATH)
final_list = []
for item in dir_list:
    file_path = PATH + "/" + item
    data = pd.read_csv(file_path, header=None)
    df_to_list = data.values.tolist()
    for line in df_to_list:
        final_list.append(line)

df = pd.DataFrame(final_list)
df.to_csv(SAVE_PATH, header=None, index=None, encoding='utf-8-sig')
print("Finished writing file ", SAVE_PATH)
print(len(df))