import os
import random
import pandas as pd

# KISA Path
KISA_PATH = "./data/KISA/preprocessed/KISA_SPAM.csv"
# AIHUB Path
AIHUB_PATH = "./data/한국어_SNS/preprocessed/AIHUB_NONSPAM.csv"
# FINAL Path
SAVE_PATH = "./data/Korean/Korean_Spam_and_Nonspam.csv"

final_list = []
data = pd.read_csv(KISA_PATH, header=None)
df_to_list = data.values.tolist()
for line in df_to_list:
    final_list.append(line)
    
data = pd.read_csv(AIHUB_PATH, header=None)
df_to_list = data.values.tolist()
for line in df_to_list:
    final_list.append(line)

# 0과 1 섞기
random.shuffle(final_list)

df = pd.DataFrame(final_list)
df.to_csv(SAVE_PATH, header=['is_spam', 'text'], index=None, encoding='utf-8-sig')
print("Finished writing file ", SAVE_PATH)
print(len(df))