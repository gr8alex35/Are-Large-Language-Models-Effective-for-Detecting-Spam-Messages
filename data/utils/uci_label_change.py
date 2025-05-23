import os
import random
import pandas as pd

PATH = "./data/uci_spam.csv"

df = pd.read_csv(PATH)
df.loc[df['is_spam'] == 'spam', 'is_spam'] = 1
df.loc[df['is_spam'] == 'ham', 'is_spam'] = 0
print(df)
df.to_csv(PATH, index=None, encoding='utf-8-sig')