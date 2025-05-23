import pandas as pd

MODEL_NAME = "HyperCLOVA" # chatGPT HyperCLOVA gemini
SHOT = "zero-shot" # zero-shot one-shot three-shot five-shot new_few-shot
METHOD = "method_1" # method_1 method_2 method_3
FILE_NAME = "Korean_Spam_and_Nonspam.csv" # Korean_Spam_and_Nonspam uci_spam new_English_Spam_and_Nonspam

PATH = "./results/"+ MODEL_NAME+"/"+ METHOD + "/"+ SHOT+"/"+FILE_NAME[:-4]+"_"+ MODEL_NAME +"_res_filtered.csv"

tp, fp, fn, tn = 0,0,0,0

df = pd.read_csv(PATH, header=None, encoding='utf-8-sig')
# [0]: index, [1]: label, [2]: text, [3]: response, [4]: final_response

# 일단 response 종류 모두 확인해보기 (unique한 list 만들어보자)
responses = df[4].values.tolist()
print(len(responses))
print(set(responses))

for i in range(len(df)):
    label = str(df[1][i])
    response = str(df[4][i])
    if label == '1' and response == '1':
        tp += 1
    elif label != '1' and response == '1':
        fp += 1
    elif label == '1' and response != '1':
        fn += 1
    else:
        tn += 1

precision = tp / (tp+fp)
recall = tp / (tp+fn)
f1 = 2 * (precision*recall)/(precision+recall+1e-4)
acc = (tp+tn)/(tp+tn+fp+fn)

fpr = fp / (fp + tn)
fnr = fn / (fn + tp)

print("results for ",PATH)
print("acc: ", round(acc, 8))
print("f1: ", round(f1, 8))
print("precision: ", round(precision, 8))
print("recall: ", round(recall, 8))
print(f"\nfpr: {fpr:8f}\nfnr: {fnr:8f}")
print()
print(f"tp: {tp}\nfp: {fp}\nfn: {fn}\ntn: {tn}\ntotal: {len(responses)}")
print()
print(MODEL_NAME, SHOT, METHOD)
print(FILE_NAME)