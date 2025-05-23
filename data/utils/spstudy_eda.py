import os
import random
import pandas as pd

cwd = os.getcwd()
print("Current working directory:", cwd)

data_path = "./data/spstudy-main/Data/super_sms_dataset.csv"

df = pd.read_csv(data_path, encoding='cp437')

# Rename a single column
df = df.rename(columns={'Labels': 'is_spam', 'SMSes':'text'})
# Drop rows with NaN values
df.dropna(inplace=True)
df.reset_index(drop=True, inplace=True)  # Reset index # This is important. Needs to reset the index for rows

print(type(df['is_spam'][0]))
df['is_spam'] = df['is_spam'].astype('int64')
print(type(df['is_spam'][0]))

# Count the number of 1s
count_ones = df['is_spam'].sum()
total = len(df)

print(f"Number of 1s (spams): {count_ones}.  Percentage: {float(count_ones)/total*100}%")
print(f"Number of 0s (normal): {count_ones}. Percentage: {(1-float(count_ones)/total)*100}%")


## I want to make a 50 to 50 English dataset. And also, match the number of the korean dataset for fun issues.
## The number of korean dataset: 19965 = 9997 (1s) + 9968 (0s)

spam_index = []
normal_index = []
# print(len(df)) # 67008
for i in range(len(df)):
    if df['is_spam'][i] == 1: 
        spam_index.append(i)
    else: 
        normal_index.append(i)

print(len(spam_index), len(normal_index)) # 26178 40830

import random

# Extract 10,000 random values from each list
sampled_spam = sorted(random.sample(spam_index, 10000))
sampled_normal = sorted(random.sample(normal_index, 10000))

# Print the results
print("Sampled spam indices:", len(sampled_spam))
print("Sampled normal indices:", len(sampled_normal))


# Create new DataFrames for spam and normal
spam_df = df.iloc[sampled_spam]
normal_df = df.iloc[sampled_normal]

# Concatenate the DataFrames
combined_df = pd.concat([spam_df, normal_df])

# Shuffle the rows
shuffled_df = combined_df.sample(frac=1, random_state=42).reset_index(drop=True)

# Print the resulting DataFrame
# Assuming your DataFrame is named df
shuffled_df = shuffled_df[['is_spam', 'text']]
print(shuffled_df.head())
print(len(shuffled_df))

# FINAL Path
SAVE_PATH = "./data/new_English_Spam_and_Nonspam.csv"
shuffled_df.to_csv(SAVE_PATH, header=['is_spam', 'text'], index=None, encoding='utf-8-sig')
print("Finished writing file ", SAVE_PATH)
print(len(shuffled_df))