# Refer to this blog for more information: https://sunshower99.tistory.com/35
import google.generativeai as genai
import os
# Suppress logging warnings for GEMINI
os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"

import time
import random
from datetime import datetime
import pandas as pd

import sys
sys.path.append('./data/utils/')
from csv_to_excel import make_excel, make_csv

# Set Parameters
API_KEY= ''                                     # Place your API_KEY here
MODEL_NAME = "gemini"
SHOT = "one-shot"                               # zero-shot one-shot three-shot new_few-shot five-shot
METHOD = "method_3"                             # method_1 method_2 method_3
FILE_NAME = "Korean_Spam_and_Nonspam.csv"       # Korean_Spam_and_Nonspam uci_spam new_English_Spam_and_Nonspam

# Timeout and Index Information
TIMEOUT_MIN = 0
TIMEOUT_MAX = 0
START_INDEX = 0
END_INDEX = 19965

# PATH Information
FILE_PATH = "./data/"+FILE_NAME
SAVE_PATH = "./results/"+ MODEL_NAME+"/"+ METHOD + "/"+ SHOT+"/"+FILE_NAME[:-4]+"_"+ MODEL_NAME +"_response.csv"

# Prompts
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from prompts import *

SUFFIX = """\nAnswer should be less than 50 tokens."""

# Frequent API calls can lead to 500 internal error
# Therefore monitoring is required
def get_timeout(min, max):
    return random.randint(min, max)

# gemini configuration
genai.configure(api_key=API_KEY)
safety_settings = [
    {
        "category": "HARM_CATEGORY_DANGEROUS",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    },
]
model = genai.GenerativeModel('gemini-1.5-flash-8b', safety_settings=safety_settings) # Using gemini-1.5-flash-8b

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
    input_text += SUFFIX
    # Send an API request and get a response.
    response = model.generate_content(input_text)
    
    prompt_feedback = str(response.prompt_feedback)
    if prompt_feedback[:5] == "block": # When unsafe and unethical content is generated
        response_list.append([i, input_text, "No content due to safety and ethical reason [minseok]"])
        # Append Response in CSV file
        make_csv(SAVE_PATH, i, [i, input_text, "No content due to safety and ethical reason [minseok]"])
        print("Handled unsafety content")
    
    else:    
        response_list.append([i, label_list[i], input_text, response.text])
        # Append Response in CSV file
        make_csv(SAVE_PATH, i, [i, label_list[i], input_text, response.text])
    
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
print("=== GEMINI FINISHED ===")
print(f"Method: {METHOD}")
print(f"Shot: {SHOT}")
print(f"File name: {FILE_NAME}")
print(f"Save path: {SAVE_PATH}")