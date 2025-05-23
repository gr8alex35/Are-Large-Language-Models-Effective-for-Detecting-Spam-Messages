import pandas as pd
import csv
# Korean_Spam_and_Nonspam_gemini_response  uci_spam_gemini_response
csv_path = "./results/gemini/uci_spam_gemini_response.csv"
def make_excel(csv_path):
    csv_name = csv_path[:-4]
    read_file = pd.read_csv (csv_name+'.csv')
    read_file.to_excel (csv_name+'.xlsx', index = True, header=False)
    print("Successfully turned csv to xlsx file.")
    print(csv_path)
    return
make_excel(csv_path)