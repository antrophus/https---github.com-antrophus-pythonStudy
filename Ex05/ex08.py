'''
1. 최소버전 + 토큰값
---
2. 이전 내역 기억하기
role : system / assistant / user
---
3. 사용자 질문 입력하기
---
4. 반복해서 질문 입력하기, 종료가능. *대화내용이 누적되지 않음
---
5. 반복해서 질문 입력하기, 대화내용 누적 --> 토큰(비용) 사용량이 많아짐.
---
6. system 배경(1)+질문+답변(5*2) --> 11개만 보관 (토큰 사용량 절약)
---
7. system 사이트정보 추가
---
8. 사이트정보 함수로 호출하기
'''

import os         # os 모듈을 사용해서 환경변수에 접근
from openai import OpenAI
import chat_dao as dao

# 저장할 메시지 개수
n = 11

# api 키를 os에 저장된 환경변수에서 불러옴
openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key = openai_api_key)

#system 프로프트
prompt_txt = dao.get_data()

message_history = [
  {"role":"system","content": prompt_txt}
]

#사용자로부터 질문 입력 받기
print("*"*50)
print("*"*2," "*5, "반갑습니다. 질문을 입력해 주세요", " "*5, "*"*2)
print("*"*50)

while True:
  
  question = input("(사용자): ")
  if question != "\q":
    #메시지
    message_history.append({"role":"user","content": question})

    if len(message_history) > n:
      message_history = [message_history[0]] + message_history[-(n-1):] # 0번째 리스트는 유지 + 뒤에서 10번째 리스트부터 끝까지의 데이터 유지
      print(f"{message_history}\n")

    response = client.chat.completions.create(
      model="gpt-3.5-turbo-0125",
      messages= message_history,
      temperature=1,
      max_tokens=2048,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0,
      response_format={
        "type": "text"
      }
    )
    print(f"[챗_GPT]: {response.choices[0].message.content}")
    message_history.append({"role":"assistant","content": response.choices[0].message.content})
    
  else:
    print("*"*50)
    print("*"*2," "*16, "감사합니다.", " "*15, "*"*2)
    print("*"*50)
    break
  # print(response.choices[0].message.content)


