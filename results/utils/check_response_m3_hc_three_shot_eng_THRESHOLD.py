"""
This script is designed to cleanly convert model responses into numerical labels.

- It opens each results.csv file to review the responses.
- If a response starts with a number and the number is one of 0, 1, 2, or 3, that number is saved as the final label.
- If a response does not start with a number, the user is prompted to read the given prompt and response, then manually input the final label.
- A safety check is in place to ensure that the input is a valid number; if not, the user is asked to input again.
- If the user inputs "Q" or "q" at any point, the script stops and saves all progress made so far.

Note: 
- In the case of method_3, the model is instructed to respond with a number from 10 to 1, where 10 means spam and 1 means normal.
- You can freely comment out code in line 74 and 76 when processing the data.

"""

import re
import pandas as pd

MODEL_NAME = "HyperCLOVA"                           # chatGPT HyperCLOVA
SHOT = "five-shot"                                  # zero-shot one-shot three-shot new_few-shot five-shot
METHOD = "method_3"                                 # method_1 method_2 method_3
FILE_NAME = "new_English_Spam_and_Nonspam.csv"      # Korean_Spam_and_Nonspam uci_spam new_English_Spam_and_Nonspam

PATH = "./results/"+ MODEL_NAME+"/"+ METHOD + "/"+ SHOT+"/"+FILE_NAME[:-4]+"_"+ MODEL_NAME +"_response.csv"

SAVE_PATH = "./results/"+ MODEL_NAME+"/"+ METHOD + "/"+ SHOT+"/"+FILE_NAME[:-4]+"_"+ MODEL_NAME +"_res_filtered.csv"

# Using regular expressions
def extract_first_number_after_two(text):
    pattern = r"6\.[^\d]*(\d+)"
    match = re.search(pattern, text, re.MULTILINE)
    return match.group(1) if match else None

def find_first_number_or_sentence(sentence):
    match = re.search(r'\d+', sentence)
    return int(match.group()) if match else sentence

def extract_spam_score_eng1(text):
    match = re.search(r'(6번 문자|6th message).*?(\d+)점?', text, re.DOTALL)
    if match:
        return int(match.group(2))
    return None

# Return None if number doesn't exist
def extract_spam_score_eng2(text):
    match = re.search(r'scale of 10 to\s*(\d+)', text)
    if match:
        return int(match.group(1))
    return None  

def find_first_number_after_n_char(text):
    pattern = r"6번 문자.*?(\d+)"
    match = re.search(pattern, text, re.DOTALL)
    
    return match.group(1) if match else None


def extract_first_number(text):
    pattern = r"\b(\d+)\b"
    match = re.search(pattern, text)
    if match:
        return match.group(1)
    return None

# Based on the content of the message, it appears to be promoting a property deal and offers free booking along with other attractive incentives. Therefore, I would classify this message as spam on a scale of 10 to 1, with a score of 10.
def extract_scale_number(text):
    pattern = r"on a scale of 10 to 1.*?(\d+)"
    match = re.search(pattern, text)
    if match:
        return match.group(1)
    return None

# Use this code in the first processing (It creates the csv file)
df = pd.read_csv(PATH, header=None, encoding='utf-8-sig')
# Use this code in after the first processing (It uses the created csv file)
# df = pd.read_csv(SAVE_PATH, header=None, encoding='utf-8-sig')
# [0]: index, [1]: label, [2]: text, [3]: response [4]: final_response
if list(df.columns) == [0, 1, 2, 3]:
    df[4] = [-1]*len(df)

print("Opened file ", SAVE_PATH)
for i in range(len(df)):
    # response가 'str' 형태로 저장되어 있음
    prompt = df[2][i]
    response = df[3][i]
    if df[4][i] != -1:
        continue
    
    if response in ['0','1','2','3','4','5','6','7','8','9','10']:
        df.loc[i, 4]=response
    
    elif extract_spam_score_eng1(response) in [0,1,2,3,4,5,6,7,8,9,10]:
        df.loc[i, 4]=str(extract_spam_score_eng1(response))
    elif extract_spam_score_eng2(response) in [0,1,2,3,4,5,6,7,8,9,10]:
        df.loc[i, 4]=str(extract_spam_score_eng2(response))
    elif find_first_number_or_sentence(response) in [0,1,2,3,4,5,6,7,8,9,10]:
        df.loc[i,4]=str(find_first_number_or_sentence(response))
    
    elif response[:2] == '6.':
        if extract_first_number_after_two(response) in ['0','1','2','3','4','5','6','7','8','9','10']:
            df.loc[i,4]=extract_first_number_after_two(response)
        else:
            print("index", i)
            print(response)
            df.loc[i,4]='0'
    
    elif ":" in response:
        response_new = response.split(":")[1]
        if response_new[:2] != "\n6":
            if extract_first_number(response_new) in ['0','1','2','3','4','5','6','7','8','9','10']:
                df.loc[i,4]=extract_first_number(response_new)
            else:
                print("index", i)
                print(response)
                df.loc[i,4]='0'
                
        elif response_new[:2] == "\n6":
            new_text = response_new[2:]
            if extract_first_number(new_text) in ['0','1','2','3','4','5','6','7','8','9','10']:
                df.loc[i,4]=extract_first_number(new_text)
            else:
                print("index", i)
                print(response)
                df.loc[i,4]='0'       
        else:
            print("!! Error")   
            print("index", i)
            print(response)
            print(response_new)      
            
    elif "→" in response: # Exception case
        response = response.split("→")[-1]
        if len(response) == 0:
            df.loc[i,4] = '0'
        if response[1] in ['5','6','7','8','9']:
            df.loc[i, 4]=response[1] 
        elif response[1:3] in ['10']:
            df.loc[i, 4]='10' 
        else:
            print("Case: →")
            print("index", i)
            print(response)
            df.loc[i,4]='0'       
    elif "⇒" in response: # Exception case
        response = response.split("⇒")[-1]
        if len(response) == 0:
            df.loc[i,4] = '0'
        elif response[1] in ['5','6','7','8','9']:
            df.loc[i, 4]=response[1]
        elif response[1:3] in ['10']:
            df.loc[i, 4]='10'
        else:
            print("Case: ⇒")
            print("index", i)
            print(response)
            df.loc[i,4]='0'   
    
    elif extract_scale_number(response) in ['0','1','2','3','4','5','6','7','8','9','10']:
            df.loc[i,4]=extract_scale_number(response)
    
    elif response[:14] == "Please provide":
        df.loc[i,4]='0'
    elif response[:12] == "Insufficient":
        df.loc[i,4]='0'
    elif response[:9] == "Difficult":
        df.loc[i,4]='0'
    elif response[:6] == "Unable":
        df.loc[i,4]='0'
    elif response[:5] == "죄송합니다":
        df.loc[i,4]='0'
    elif response[:5] == "문자 내용":
        df.loc[i,4]='0'
    elif response[:3] == "문맥이":
        df.loc[i,4]='0'
        
    else:
        
        while(1):
            print("================================================================")
            print("<index>: ", i)
            print("<prompt>: ", prompt)
            print("\n<response>: ", response)
            print("<final_response>: ", df[4][i])
            print("Please enter final response 0 or `[not a spam], 1[is a spam], 2[IDK] (Q or q for save and quit): ", end='')
            fr = input() # fr: final_response
            if fr in ['0','1','2','3','4','5','6','7','8','9','10']:
                df.loc[i, 4]=fr
                break
            elif fr == '`': # For easier input
                df.loc[i,4]='0'
                break
            elif fr == 'Q' or fr == 'q':
                df.loc[i, 4]=-1
                df.to_csv(SAVE_PATH, header=None, index=None, encoding='utf-8-sig')
                print(f"Successfully saved to {SAVE_PATH} and quit.")
                quit() # Terminate program

print("Finished filtering responses.")
df.to_csv(SAVE_PATH, header=None, index=None, encoding='utf-8-sig')
print(f"Successfully saved to {SAVE_PATH} and quit.")
print(MODEL_NAME, SHOT, METHOD, FILE_NAME)