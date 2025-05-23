"""
This script is designed to cleanly convert model responses into numerical labels.

- It opens each results.csv file to review the responses.
- If a response starts with a number and the number is one of 0, 1, 2, or 3, that number is saved as the final label.
- If a response does not start with a number, the user is prompted to read the given prompt and response, then manually input the final label.
- A safety check is in place to ensure that the input is a valid number; if not, the user is asked to input again.
- If the user inputs "Q" or "q" at any point, the script stops and saves all progress made so far.

Note: 
- In the case of method_3, the model is instructed to respond with a number from 10 to 1, where 10 means spam and 1 means normal.
- You can freely comment out code in line 33 and 35 when processing the data.

"""

import re
import pandas as pd

MODEL_NAME = "chatGPT"                          # chatGPT HyperCLOVA
SHOT = "one-shot"                               # zero-shot one-shot few-shot new_few-shot five-shot
METHOD = "method_1"                             # method_1 method_2 method_3
FILE_NAME = "Korean_Spam_and_Nonspam.csv"       # Korean_Spam_and_Nonspam uci_spam new_English_Spam_and_Nonspam

PATH = "./results/"+ MODEL_NAME+"/"+ METHOD + "/"+ SHOT+"/"+FILE_NAME[:-4]+"_"+ MODEL_NAME +"_response.csv"

SAVE_PATH = "./results/"+ MODEL_NAME+"/"+ METHOD + "/"+ SHOT+"/"+FILE_NAME[:-4]+"_"+ MODEL_NAME +"_res_filtered.csv"

def find_first_number_or_sentence(sentence):
    match = re.search(r'\d+', sentence)
    return int(match.group()) if match else sentence

# Use this code in the first processing (It creates the csv file)
df = pd.read_csv(PATH, header=None, encoding='utf-8-sig')
# Use this code in after the first processing (It uses the created csv file)
df = pd.read_csv(SAVE_PATH, header=None, encoding='utf-8-sig')
# [0]: index, [1]: label, [2]: text, [3]: response [4]: final_response
if list(df.columns) == [0, 1, 2, 3]:
    df[4] = [-1]*len(df)

# Phrases used in spam-classified response
spam_list = [
    '스펨 메시지일 가능성이 높',
    '스펨 문자일 가능성이 높',
    '스펨일 가능성이 높',
    '스팸입니',
    '스팸 문자입니',
    '스팸 메시지입니',
    '스팸에 가깝습니다',
    '스팸에 가까운',
    '스팸에 가까울',
    '스팸에 가깝',
    '스팸에 매우 가',
    '스팸으로 분류될 가능성이 높',
    '스팸으로 판단',
    '스팸으로 간주',
    '스팸으로 구분',
    '스팸으로 분류','스팸으로 추정',
    '스팸일 가능성이 높',
    '스팸일 가능성이 매우 높',
    '스팸 문자일 가능성이 높',
    '스팸 문자일 가능성이 매우 높',
    '스팸 메시지일 가능성이 높',
    '스팸 메시지일 가능성이 매우 높',
    '스팸일 가능성이 있',
    '스팸 뮨자일 가능성이 있',
    '스팸 메시지일 가능성이 있',
    '스팸문자로 판단',
    '스팸 문자로 판단',
    '스팸 메시지로 분류할 수 있',
    '스팸의 특징을 가',
    '스팸의 특징을 갖',
    '스팸 메시지에서 흔히 나타나는',
    '스팸 문자에서 흔히 나타나는',
    '스팸에서 흔히 나타나는',
    '스팸으로 인식될',
    '스팸에 더 가까',
    '스팸에 매우 가까',
    '스팸 메시지의 특징을 가',
    '스팸 문자의 특징을 가', 
    '스팸의 특징을 많이 가',
    '스팸 문자의 특징을 많이 가',
    '스팸 메시지의 특징을 많이 가',
    '판촉 메시지에서 나타나는 패턴',
    '광고성 메시지로 보',
    '홍보성 메시지로 보',
    '스팸 메시지의 특징을 포함',
    '스팸 메시지의 특징을 많이 포함',
    '스팸 문자의 특징을 포함',
    '스팸 문자의 특징을 많이 포함',
    '스팸 문장의 특징을 포함',
    '스팸 문장의 특징을 많이 포함',
    '스팸의 특징을 포함',
    '스팸의 특징을 많이 포함',
    '스팸 메시지로 보',
    '스팸 문자로 보',
    '스팸으로 보',
    '스팸 메시지의 일반적인 특징을 가',
    '스팸 문자의 일반적인 특징을 가',
    '스팸의 일반적인 특징을 가',
    '스팸 메시지의 특징을 보',
    '스팸 문자자의 특징을 보'
    '스팸 메시지의 특징을 많이 보',
    '스팸의 특징을 많이 보',
    '매우 스팸성으로 보',
    '스팸으로 보일 가능성이 높',
    '스팸 문자로 보일 가능성이 높',
    '스팸 메시지로 보일 가능성이 높',
    '스팸 메시지에서 흔히 볼 수 있는 특징',
    '스팸 문자에서 발견되는 특',
    '스팸 메시지에서 발견되는 특',
    '스팸에서 발견되는 특',
    '스팸 메시지의 특성을 가',
    '스팸 문자의 특성을 가',
    '스팸의 특성을 가',
    '스팸의 특징이 나타',
    '스팸 메시지의 특징이 나타',
    '스팸 문자의 특징이 나타',
    '스팸 메시지의 특징입',
    '스팸 문자의 특징입',
    '스팸의 특징입',
    '스팸에 해당',
    '스팸 문자에 해당',
    '스팸 메시지에 해당',
    '스팸 메시지로 분류',
    '스팸 문자로 분류',
    '스팸으로 분류',
    '스팸 메시지로 판단',
    '스팸 문자로 판단',
    '스팸으로 판단',
    '스팸으로 간주',
    '스팸 문자로 간주',
    '스팸 메시지로 간주',
    '스팸으로 의심',
    '스팸 문자로 의심',
    '스팸 메시지로 의심',
    '스팸으로 볼 수 있',
    '스팸 문자로 볼 수 있',
    '스팸 메시지로 볼 수 있',
]

# Phrases used in nonspam-classified response
non_spam_list = [
    '비스팸',
    '스팸 아님',
    '아닙니다',
    '아닌 것 같습니다',
    '일반적인 메시지입니다',
    '정상적인 메시지로 보',
    '일반적인 메시지로 보',
    '정상적인 메시지입',
    '일반적인 메시지입',
    '일반 메시지입',
    '정상 메시지입',
    '일반적인 문자입니다',
    '정상적인 문자로 보',
    '일반적인 문자로 보',
    '정상적인 문자입',
    '일반적인 문자입',
    '일반 문자입',
    '정상 문자입',
    '스팸이라기보다',
    '스팸 문자라기보다',
    '스팸 메시지라기보다',
    '스팸 메시지로 분류되지 않',
    '스팸 메시지가 아닙',
    '스팸이 아닙',
    '스팸 문자가 아닙',
    '스팸 가능성은 낮',
    '스팸과 관련된 내용이 없',
    '스팸 가능성이 낮',
    '스팸 가능성이 매우 낮',
    '스팸일 가능성이 낮',
    '스팸일 가능성이 매우 낮',
    '스팸일 가능성은 낮',
    '스팸일 가능성은 매우 낮',
    '스팸으로 보이지 않',
    '스팸으로 보이진 않',
    '스팸 여부를 판단하기 어',
    '스팸으로 보기는 어',
    '스팸과는 관련이 없',
    '판단하는 것은 매우 복잡한',
    '스팸으로 분류될 가능성이 낮',
    '스팸 점수는 0',
    '스팸 점수는 1에',
    '스팸 점수는 2',
    '스팸 점수는 3',
    '스팸 점수는 4',
    '점수를 0',
    '점수를 1에',
    '점수를 2',
    '점수를 3',
    '점수를 4',
    ' 0에 가',
    '스팸과 거리가 멀',
    '스팸과는 거리가 멀',
    '스팸이 아닐 가능성이 높',
    '스팸이 아닐 가능성이 매우 높',
    '스팸이 아',
    '죄송',
    '일반적인 대화의 일부',
    '일반적인 문장으로 보',
    '일반적인 문자로 보',
    '정상적인 메시지에 가',
    '정상적인 문자에 가',
    '정상적인 문장에 가',
    '개인적인 대화에 가',
    '일상적인 대화에 가',
    '일상적인 문장에 가',
    '일상적인 문자에 가',
    '일상적인 메시지에 가',
    '일반적인 대화의',
    '일상적인 대화의',
    '일반적인 대화로',
    '일상적인 대화로',
    '답변을 드리기 어',
    '판단이 어',
    '판단하기 어',
    '판단할 수 없',
    '분류하는 것은 매우 복잡한','분류가가 어',
    '분류하기 어', '분류할 수 없',
    '분류할 수 없',
    '분류할 수 없',
    '구분하는 것은 매우 복잡한',
    '구분이 어',
    '구분하기 어',
    '구분할 수 없',
    '문자 내용을 알려',
    '문자 내용을 알려',
    '여부를 판단하기 위',
    '스팸 여부를 판단하는 것은 매우 복잡한',
    '불가능',
    '스팸 여부',
    '스팸인지 아닌지',
    '정보가 필요',
    '판단할 수 있는 기준',
    '정상 문자',
    '정상적인 문장',
    '어떤 문자', 
    '데이터가 필요',
    '파악하기 어',
    '알고리즘이 필',
    '문법적으로 올바르지 않',
    '제공할 수 없',
    '내리기 어',
    '데이터셋을 수집',
    '데이터를 수집',
    '일상적인 대화로 보',
    '정보가 부족',
    '스팸과 관련이 없',
    '스팸성은 낮',
]

print("Opened file ", SAVE_PATH)
for i in range(len(df)):
    # response is saved in 'str' format
    prompt = df[2][i]
    response = df[3][i]
    # If the response is already labeled, continue
    if df[4][i] != -1:
        continue
    
    flag_found = 0
    # Search the non_spam_list
    for j in range(len(non_spam_list)):
        if non_spam_list[j] in response:
            df.loc[i, 4]='0'
            flag_found = 1
            break
    if flag_found != 1:
        # Search the spam_list
        for j in range(len(spam_list)):
            if spam_list[j] in response:
                df.loc[i, 4]='1'
                flag_found = 1
                break
    if flag_found != 1:
        if response in ['1','2','3','4']:
            df.loc[i, 4]='0'
        elif find_first_number_or_sentence(response) in [1,2,3,4]:
            df.loc[i, 4]='0'
        
        elif "Please provide" in response:
            df.loc[i,4]='0'
        elif "Insufficient" in response:
            df.loc[i,4]='0'
        elif "Difficult" in response:
            df.loc[i,4]='0'
        
        
        elif "아닌 스팸" in response:
            df.loc[i,4]='0'
        elif "일반 문자" in response:
            df.loc[i,4]='0'
        elif "일반 메시지" in response:
            df.loc[i,4]='0'
            
        elif "스팸" in response:
            df.loc[i,4]='1'
        elif response in ['5','6','7','8','9','10']:
            df.loc[i, 4]='1'
        elif response[0] in ['5','6','7','8','9','10']:
            df.loc[i, 4]='1' 
        elif find_first_number_or_sentence(response) in [5,6,7,8,9,10]:
            df.loc[i, 4]='1'
        
        else:
            while(1):
                print("================================================================")
                print("<index>: ", i)
                print("<prompt>: ", prompt)
                print("\n<response>: ", response)
                print("<final_response>: ", df[4][i])
                print("Please enter final response 0 or `[not a spam], 1[is a spam], 2[IDK] (Q or q for save and quit): ", end='')
                fr = input() # fr: final_response
                if fr in ['0','1']:
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