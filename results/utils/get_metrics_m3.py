import pandas as pd

MODEL_NAME = "chatGPT" # chatGPT HyperCLOVA gemini
SHOT = "five-shot" # zero-shot one-shot three-shot five-shot
METHOD = "method_3" # method_1 method_2 method_3
FILE_NAME = "Korean_Spam_and_Nonspam.csv" # Korean_Spam_and_Nonspam uci_spam new_English_Spam_and_Nonspam

PATH = "./results/"+ MODEL_NAME+"/"+ METHOD + "/"+ SHOT+"/"+FILE_NAME[:-4]+"_"+ MODEL_NAME +"_res_filtered.csv"

THRESHOLD = 2

tp, fp, fn, tn = 0,0,0,0

label_counter = {"-1":0, "0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "10":0}

df = pd.read_csv(PATH, header=None, encoding='utf-8-sig')
# [0]: index, [1]: label, [2]: text, [3]: response, [4]: final_response

# 일단 response 종류 모두 확인해보기 (unique한 list 만들어보자)
responses = df[4].values.tolist()
print(len(responses))
print(set(responses))



for i in range(len(df)):
    label = str(df[1][i])
    response = str(df[4][i])
    label_counter[response] += 1
    if int(response) < THRESHOLD:
        response = '0'
    else:
        response = '1'
    
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

for key in label_counter.keys():
    print(f"{key}: {label_counter[key]}")

print()
print(MODEL_NAME, SHOT, METHOD)
print(FILE_NAME)