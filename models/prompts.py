"""
Prompt: Task description + Sample message(s) + Input text

KOR_PROMPT_1, ENG_PROMPT_1, KOR_PROMPT_2, ENG_PROMPT_2, KOR_PROMPT_3, ENG_PROMPT_3,
ONE_SHOT_KOR_PROMPT, ONE_SHOT_ENG_PROMPT, ONE_SHOT_KOR_PROMPT_3, ONE_SHOT_ENG_PROMPT_3,
THREE_SHOT_KOR_PROMPT, THREE_SHOT_ENG_PROMPT, THREE_SHOT_KOR_PROMPT_2, THREE_SHOT_ENG_PROMPT_2, THREE_SHOT_KOR_PROMPT_3, THREE_SHOT_ENG_PROMPT_3,
FIVE_SHOT_KOR_PROMPT, FIVE_SHOT_ENG_PROMPT, FIVE_SHOT_KOR_PROMPT_3, FIVE_SHOT_ENG_PROMPT_3
"""

# prompts (zero-shot)
KOR_PROMPT_1 = "문자 내용이 스팸인지 아닌지 구분하시오.\n"
ENG_PROMPT_1 = "Detect whether the following message is spam or not.\n"
KOR_PROMPT_2 = "숫자로 답변해줘. 다음 문자 내용이 스팸이면 1, 아니면 0, 모르겠으면 2, 대답을 못하겠으면 3.\n"
ENG_PROMPT_2 = "Respond using the following labels only. If the following message is spam, 1. If not 0. If you are not sure, 2. If you cannot answer 3.\n"
KOR_PROMPT_3 = "10부터 1 사이의 숫자로 문자 내용이 스팸인지 아닌지 구분하시오 (스팸에 가까우면 10, 정상 문자에 가까우면 0).\n"
ENG_PROMPT_3 = "Using a scale 10 to 1, detect whether the following message is spam or not (10 for spam, 1 for non-spam).\n"

# one-shot
ONE_SHOT_KOR_PROMPT = """문자 내용이 스팸인지 아닌지 구분하시오.
11월 첫이용자EVENT♥ 5+4+⑴1O+7+⑵COMP까지!라카지노abit.ly/vylsxt오늘방문하세요!! ⇒ 스팸
"""
ONE_SHOT_ENG_PROMPT = """Detect whether the following message is spam or not.
WINNER!! As a valued network customer you have been selected to receivea £900 prize reward! ⇒ Spam
"""
ONE_SHOT_KOR_PROMPT_3 = """2번 문자가 스팸인지 아닌지 문자 반복하지 말고 10부터 1 사이의 점수로만 답해줘 (스팸 문자면 10점, 정상 문자면 1점).
1. 11월 첫이용자EVENT♥ 5+4+⑴1O+7+⑵COMP까지!라카지노abit.ly/vylsxt오늘방문하세요!! ⇒ 10점
"""
ONE_SHOT_ENG_PROMPT_3 = """Using a scale 10 to 1, detect whether the 2nd message is spam or not (10 for spam, 1 for non-spam).
1. WINNER!! As a valued network customer you have been selected to receivea £900 prize reward! ⇒ 10
"""

# three-shot
THREE_SHOT_KOR_PROMPT = """문자 내용이 스팸인지 아닌지 구분하시오.
11월 첫이용자EVENT♥ 5+4+⑴1O+7+⑵COMP까지!라카지노abit.ly/vylsxt오늘방문하세요!! ⇒ 스팸
으아 배고프다 ⇒ 스팸 아님
안녕하세요 회원님이전 이용하신 놀이터에서 새롭게 단장한 발롱도르에서 보유하고 계셨던 보유금 이관 안내드립니다.앞전 이용하셨던 보유금 전체 이관되셨으니 발롱도르 입장하신 후 확인바라며 사용 및 환 신청 해주시길 바랍니다.잔금 382 ⇒ 스펨
"""
THREE_SHOT_ENG_PROMPT = """Detect whether the following message is spam or not.
WINNER!! As a valued network customer you have been selected to receivea £900 prize reward! ⇒ Spam
Nah I don't think he goes to usf, he lives around here though ⇒ Not spam
Had your mobile 11 months or more? U R entitled to Update to the latest colour mobiles with camera for Free! Call The Mobile Update Co FREE on 08002986030 ⇒ Spam
"""
THREE_SHOT_KOR_PROMPT_2 = """숫자로 답변해줘. 다음 문자 내용이 스팸이면 1, 아니면 0, 모르겠으면 2, 대답을 못하겠으면 3.
11월 첫이용자EVENT♥ 5+4+⑴1O+7+⑵COMP까지!라카지노abit.ly/vylsxt오늘방문하세요!! ⇒ 스팸
으아 배고프다 ⇒ 스팸 아님
안녕하세요 회원님이전 이용하신 놀이터에서 새롭게 단장한 발롱도르에서 보유하고 계셨던 보유금 이관 안내드립니다.앞전 이용하셨던 보유금 전체 이관되셨으니 발롱도르 입장하신 후 확인바라며 사용 및 환 신청 해주시길 바랍니다.잔금 382 ⇒ 스펨
"""
THREE_SHOT_ENG_PROMPT_2 = """Respond using the following labels only. If the following message is spam, 1. If not 0. If you are not sure, 2. If you cannot answer 3.
WINNER!! As a valued network customer you have been selected to receivea £900 prize reward! ⇒ Spam
Nah I don't think he goes to usf, he lives around here though ⇒ Not spam
Had your mobile 11 months or more? U R entitled to Update to the latest colour mobiles with camera for Free! Call The Mobile Update Co FREE on 08002986030 ⇒ Spam
"""
THREE_SHOT_KOR_PROMPT_3 = """4번 문자가 스팸인지 아닌지 문자 반복하지 말고 10부터 1 사이의 점수로만 답해줘 (스팸 문자면 10점, 정상 문자면 1점).
1. 11월 첫이용자EVENT♥ 5+4+⑴1O+7+⑵COMP까지!라카지노abit.ly/vylsxt오늘방문하세요!! ⇒ 10점
2. 으아 배고프다 ⇒ 1점
3. 안녕하세요 회원님이전 이용하신 놀이터에서 새롭게 단장한 발롱도르에서 보유하고 계셨던 보유금 이관 안내드립니다.앞전 이용하셨던 보유금 전체 이관되셨으니 발롱도르 입장하신 후 확인바라며 사용 및 환 신청 해주시길 바랍니다.잔금 382 ⇒ 10점
"""
THREE_SHOT_ENG_PROMPT_3 = """Using a scale 10 to 1, detect whether the 4th message is spam or not (10 for spam, 1 for non-spam).
1. WINNER!! As a valued network customer you have been selected to receivea £900 prize reward! ⇒ 10
2. Nah I don't think he goes to usf, he lives around here though ⇒ 1
3. Had your mobile 11 months or more? U R entitled to Update to the latest colour mobiles with camera for Free! Call The Mobile Update Co FREE on 08002986030 ⇒ 10
"""

# five-shot
FIVE_SHOT_KOR_PROMPT = """문자 내용이 스팸인지 아닌지 구분하시오.
11월 첫이용자EVENT♥ 5+4+⑴1O+7+⑵COMP까지!라카지노abit.ly/vylsxt오늘방문하세요!! ⇒ 스팸
오늘 밤에 치킨 먹으러 갈래? ⇒ 스팸 아님
안녕하세요 회원님이전 이용하신 놀이터에서 새롭게 단장한 발롱도르에서 보유하고 계셨던 보유금 이관 안내드립니다.앞전 이용하셨던 보유금 전체 이관되셨으니 발롱도르 입장하신 후 확인바라며 사용 및 환 신청 해주시길 바랍니다.잔금 382 ⇒ 스팸
으아 배고프다 ⇒ 스팸 아님
[국제발신] 리츠칼튼10+5 20+10 50+20100+40 [출회원가능]  19:00~23:00bit.ly/Ritz-칼튼 ⇒ 스팸
"""
FIVE_SHOT_ENG_PROMPT = """Detect whether the following message is spam or not.
WINNER!! As a valued network customer you have been selected to receive a £900 prize reward! ⇒ Spam
Nah I don’t think he goes to usf, he lives around here though ⇒ Not spam
Had your mobile 11 months or more? U R entitled to Update to the latest colour mobiles with camera for Free! Call The Mobile Update Co FREE on 08002986030 ⇒ Spam
I HAVE A DATE ON SUNDAY WITH WILL!! ⇒ Not spam
"Did you hear about the new ""Divorce Barbie""? It comes with all of Ken’s stuff!" ⇒ Spam
"""
FIVE_SHOT_KOR_PROMPT_3 = """6번 문자가 스팸인지 아닌지 문자 반복하지 말고 10부터 1 사이의 점수로만 답해줘 (스팸 문자면 10점, 정상 문자면 1점).
1. 11월 첫이용자EVENT♥ 5+4+⑴1O+7+⑵COMP까지!라카지노abit.ly/vylsxt오늘방문하세요!! ⇒ 10점
2. 오늘 밤에 치킨 먹으러 갈래? ⇒ 1점
3. 안녕하세요 회원님이전 이용하신 놀이터에서 새롭게 단장한 발롱도르에서 보유하고 계셨던 보유금 이관 안내드립니다.앞전 이용하셨던 보유금 전체 이관되셨으니 발롱도르 입장하신 후 확인바라며 사용 및 환 신청 해주시길 바랍니다.잔금 382 ⇒ 10점
4.으아 배고프다 ⇒ 1점
5. [국제발신] 리츠칼튼10+5 20+10 50+20100+40 [출회원가능]  19:00~23:00bit.ly/Ritz-칼튼 ⇒ 10점
"""
FIVE_SHOT_ENG_PROMPT_3 = """Using a scale 10 to 1, ONLY detect whether the 6th message is spam or not (10 for spam, 1 for non-spam).
1. WINNER!! As a valued network customer you have been selected to receive a £900 prize reward! ⇒ 10
2. Nah I don’t think he goes to usf, he lives around here though ⇒ 1
3. Had your mobile 11 months or more? U R entitled to Update to the latest colour mobiles with camera for Free! Call The Mobile Update Co FREE on 08002986030 ⇒ 10
4. I HAVE A DATE ON SUNDAY WITH WILL!! ⇒ 1
5. "Did you hear about the new ""Divorce Barbie""? It comes with all of Ken’s stuff!" ⇒ 10
"""