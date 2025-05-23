# AI HUB 한국어 SNS 데이터셋과
# KISA 한국어 스팸 문자 통합하기
# https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=114

# < Training >
# 개인및관계:   511,496 -> 1,111
# 미용과건강:   99,383  -> 1,111
# 상거래(쇼핑): 115,503 -> 1,111
# 시사교육:     89,975  -> 1,111
# 식음료:       146,620 -> 1,111
# 여가생활:     190,306 -> 1,111
# 일과_직업:     107,976 -> 1,111 (760)
# 주거와생활:   197,528 -> 1,111
# 행사:         141,205 -> 1,111

# 한국어 총 20,000 개로 구축
# AI HUB:       10,000 -> 9,999 -> (최종)10,102
# KISA:         10,000

# < AI HUB 데이터셋 보면서 느낀 점 >
# 카톡 대화이기 때문에 생각보다 한 사람이 톡을 끊어서 보내는 경우가 많았음!
# 또한, 각 json 파일별로, 예를 들어 "미용과건강.json"에서 numberOfItems가 
# 99383인데, 문장 수가 아니고 대화의 숫자임. 즉, 문장의 개수는 더 많다는 것
#
# 데이터셋을 잘 보면 대화 상대를 P01, P02로 지정했는데, 끊어 말하는 것을 하나로 이어야
# 더 자연스러운 문장이 되므로, 말하는 상대가 같은 경우에 그 문장들을 이어주는
# 전처리를 진행하겠음.
#
# -> json 파일을 더 살펴본 결과 "turnID"라는 개념이 있었음. 따라서 "turnID"가
#    같은 친구들끼리 이어주면 그냥 바로 하나의 문장이 만들어짐
#
# 또한, 각 json 별로 1,111개를 뽑아야 함. (문장의 수가...)
# 근데, 생각해보니... 대화의 수가 1,111개면 문장은 더 많아지긴 함.

import os
import pandas as pd

PATH = "./data/한국어_SNS/Training/[라벨]한국어SNS_train"
SAVE_PATH = "./data/한국어_SNS/csv/"
JUMP = 1500

dir_list = os.listdir(PATH)

for item in dir_list:
    if item != "주거와생활.json": # json 파일별로 이름을 돌리면서 직접 csv 파일 생성함
        continue
    file_path = PATH + "/" + item
    print(file_path)
    data_frame = pd.read_json(file_path)
    conversations = []
    temp_turn = "T1" # 첫 번째 대화 Turn
    temp_talk = ""
    print(len(data_frame["data"]))
    for i in range(0, len(data_frame["data"]), JUMP):
        for j in range(len(data_frame["data"][i]["body"])):
            turn = data_frame["data"][i]["body"][j]["turnID"]
            talk = data_frame["data"][i]["body"][j]["utterance"]
            # 이모티콘이나 언급(@이름)은 #로 표시했음 -> 이걸로도 다 걸러지진 않아서 일단 응급처치
            if talk[0] == "#" or talk[:1] == "#@":
                continue
            if turn == temp_turn:
                if temp_talk != "": # 첫 번째 대화일때만 공백 안 넣기
                    temp_talk += " "
                temp_talk += talk
            else:
                # 대화 Turn이 바뀔때마다 대화 추가
                conversations.append([0, temp_talk])
                temp_turn = turn
                temp_talk = talk
        # print(conversations)
        # break
    SAVE_PATH = SAVE_PATH + item[:-5]+".csv"

df = pd.DataFrame(conversations)
df.to_csv(SAVE_PATH, header=None, index=None, encoding='utf-8-sig')
print("Finished writing file ", SAVE_PATH)
print(len(conversations))