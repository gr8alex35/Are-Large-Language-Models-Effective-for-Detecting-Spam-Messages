# -*- coding: utf-8 -*-
import os
import sys
sys.path.append('./data/utils/')
from csv_to_excel import make_excel, make_csv       

import requests
import json
import time
import random
from datetime import datetime
import pandas as pd

# Set Parameters
API_KEY = ''                                        # Place your API_KEY here
MODEL_NAME = "HyperCLOVA"                           # HCX-DASH-001 is used
SHOT = "three-shot"                                 # zero-shot one-shot three-shot five-shot
METHOD = "method_2"                                 # method_1 method_2 method_3
FILE_NAME = "new_English_Spam_and_Nonspam.csv"      # Korean_Spam_and_Nonspam uci_spam new_English_Spam_and_Nonspam

# Timeout and Index Information
TIMEOUT_MIN = 0
TIMEOUT_MAX = 0
START_INDEX = 0
END_INDEX =   1                                     # 20000 19965 # 5572 Took 9 hours

# PATH Information
FILE_PATH = "./data/"+FILE_NAME
SAVE_PATH = "./results/"+ MODEL_NAME+"/"+ METHOD + "/"+ SHOT+"/"+FILE_NAME[:-4]+"_"+ MODEL_NAME +"_response.csv"

# Prompts
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from prompts import *


# Frequent API calls can lead to 500 internal error
# Therefore monitoring is required
def get_timeout(min, max):
    return random.randint(min, max)

class CompletionExecutor:
    def __init__(self, host, api_key, request_id):
        self._host = host
        self._api_key = api_key
        self._request_id = request_id

    def execute(self, completion_request):
        headers = {
            'Authorization': self._api_key,
            'X-NCP-CLOVASTUDIO-REQUEST-ID': self._request_id,
            'Content-Type': 'application/json; charset=utf-8',
            'Accept': 'text/event-stream'
        }
        response = []
        with requests.post(self._host + '/testapp/v1/chat-completions/HCX-DASH-001',
                           headers=headers, json=completion_request, stream=False) as r:
            for line in r.iter_lines():
                if line:
                    response.append(line.decode("utf-8"))
        return response
                    

if __name__ == '__main__':
    completion_executor = CompletionExecutor(
        host='https://clovastudio.stream.ntruss.com',
        api_key='Bearer ' + API_KEY,
        request_id='3718e0e690d146938875d0c44342d0f5'
    )


    # Read Data
    data = pd.read_csv(FILE_PATH)
    input_list = data["text"]       # text
    label_list = data["is_spam"]    # is_spam
    print(f'Open file: {FILE_PATH}')
    print(f'Total length of questions not empty: {len(input_list)}')
    
    # List for saving the generated response
    response_list = []
    start = time.time()
    # Create Prompt text
    for i in range(START_INDEX,END_INDEX):
        if METHOD == 'method_1':
            if SHOT == 'zero-shot':
                if FILE_NAME == 'new_English_Spam_and_Nonspam.csv':
                    input_text = ENG_PROMPT_1 + input_list[i]
                else:
                    input_text = KOR_PROMPT_1 + input_list[i]
            elif SHOT == 'one-shot':
                if FILE_NAME == 'new_English_Spam_and_Nonspam.csv':
                    input_text = ONE_SHOT_ENG_PROMPT + input_list[i] + " ⇒ "
                else:
                    input_text = ONE_SHOT_KOR_PROMPT + input_list[i] + " ⇒ "
            elif SHOT == 'three-shot':
                if FILE_NAME == 'new_English_Spam_and_Nonspam.csv':
                    input_text = THREE_SHOT_ENG_PROMPT + input_list[i] + " ⇒ "
                else:
                    input_text = THREE_SHOT_KOR_PROMPT + input_list[i] + " ⇒ "
            elif SHOT == 'five-shot':
                if FILE_NAME == 'new_English_Spam_and_Nonspam.csv':
                    input_text = FIVE_SHOT_ENG_PROMPT + input_list[i] + " ⇒ "
                else:
                    input_text = FIVE_SHOT_KOR_PROMPT + input_list[i] + " ⇒ "
        elif METHOD == 'method_2':  
            if SHOT == 'zero-shot':
                if FILE_NAME == 'new_English_Spam_and_Nonspam.csv':
                    input_text = ENG_PROMPT_2 + input_list[i]
                else:
                    input_text = KOR_PROMPT_2 + input_list[i]
            elif SHOT == 'three-shot':
                if FILE_NAME == 'new_English_Spam_and_Nonspam.csv':
                    input_text = THREE_SHOT_ENG_PROMPT_2 + input_list[i] + " ⇒ "
                else:
                    input_text = THREE_SHOT_KOR_PROMPT_2 + input_list[i] + " ⇒ "
        else:
            if SHOT == 'zero-shot':
                if FILE_NAME == 'new_English_Spam_and_Nonspam.csv':
                    input_text = ENG_PROMPT_3 + input_list[i]
                else:
                    input_text = KOR_PROMPT_3 + input_list[i]
            elif SHOT == 'one-shot':
                if FILE_NAME == 'new_English_Spam_and_Nonspam.csv':
                    input_text = ONE_SHOT_ENG_PROMPT_3 + "2. " + input_list[i] + " ⇒ "
                else:
                    input_text = ONE_SHOT_KOR_PROMPT_3 + "2. " + input_list[i] + " ⇒ "
            elif SHOT == 'three-shot':
                if FILE_NAME == 'new_English_Spam_and_Nonspam.csv':
                    input_text = THREE_SHOT_ENG_PROMPT_3 + "4. " + input_list[i] + " ⇒ "
                else:
                    input_text = THREE_SHOT_KOR_PROMPT_3 + "4. " + input_list[i] + " ⇒ "
            elif SHOT == 'five-shot':
                if FILE_NAME == 'new_English_Spam_and_Nonspam.csv':
                    input_text = FIVE_SHOT_ENG_PROMPT_3 + "6. " + input_list[i] + " ⇒ "
                else:
                    input_text = FIVE_SHOT_KOR_PROMPT_3 + "6. " + input_list[i] + " ⇒ "
        # Prompt request
        preset_text = [{"role":"system","content":""},{"role":"user","content":input_text}]
        # Request Header Information
        request_data = {
            'messages': preset_text,
            'topP': 0.8,
            'topK': 0,
            'temperature': 0.5,
            'repeatPenalty': 5.0,
            'stopBefore': [],
            'includeAiFilters': False,
            'seed': 0
        }
        
        # Execute Prompt and Retrieve the Generated Response
        response = completion_executor.execute(request_data)
        # Read the final response
        for j in range(len(response)):
            if response[j] == "event:result":
                result = response[j+1][5:]
                json_data = json.loads(result)
        # Can print our response in JSON format using: Pretty-print (optional) -> print(json.dumps(json_data, indent=4))
        response_text = json_data["message"]["content"]
        
        response_list.append([i, label_list[i], input_text, response_text])
        # Append Response in CSV file
        make_csv(SAVE_PATH, i, [i, label_list[i], input_text, response_text])
        
        # Print out verbose
        dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f'==== {i}/{len(input_list)}   {round(i/int(len(input_list)),4)*100}% -- {dt_string} ====')
        
        # Timeout
        if i%1 == 0:
            timeout = get_timeout(TIMEOUT_MIN, TIMEOUT_MAX)
            print(f'{i}/{END_INDEX} cool down. Timeout for {timeout} seconds.')
            time.sleep(timeout)
    end = time.time()
    dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(f'took {end - start:.5f} secs for {END_INDEX-START_INDEX}queries -- {dt_string}')

    # Save CSV file in excel format (optional)
    # make_excel(SAVE_PATH, FILE_NAME)

    # Finished
    print("=== CLOVA FINISHED ===")
    print(f"Method: {METHOD}")
    print(f"Shot: {SHOT}")
    print(f"File name: {FILE_NAME}")
    print(f"Save path: {SAVE_PATH}")