import pandas as pd

MODEL_NAME = "HyperCLOVA" # chatGPT HyperCLOVA
SHOT = "zero-shot" # zero-shot one-shot three-shot five-shot
METHOD = "method_3" # method_1 method_2 method_3
FILE_NAME = "Korean_Spam_and_Nonspam.csv" # Korean_Spam_and_Nonspam uci_spam new_English_Spam_and_Nonspam

PATH = "./results/"+ MODEL_NAME+"/"+ METHOD + "/"+ SHOT+"/"+FILE_NAME[:-4]+"_"+ MODEL_NAME +"_response.csv"

df = pd.read_csv(PATH, header=None)
print(df)

# 이 index 값을 확인하는 것을 잊지 말아야 함
index = 0 # 확인하려는 파일의 starting index이어야 함
for i in range(len(df)):
    if index != df[0][i]:
        print(index)
        index += 1
        break
    index += 1

print(df[df.isna( ).any(axis=1)])