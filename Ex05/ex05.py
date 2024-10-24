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
'''

import os         # os 모듈을 사용해서 환경변수에 접근
from openai import OpenAI

openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key = openai_api_key)

#system 프로프트
prompt_txt ="""
  #context
  50글자 이내로 답해주세요

  #tone
  친절한 말투로 답변해 주세요

"""
message_history = [
  {"role":"system","content": prompt_txt}
]

#사용자로부터 질문 입력 받기
print("*"*50)
print("*"*2," "*7, "반갑습니다. 질문을 입력해 주세요", " "*7, "*"*2)
print("*"*50)

while True:
  
  question = input("(사용자)")
  if question != "\q":
    #메시지
    message_history.append({"role":"user","content": question})

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
    print(f"[챗_GPT]{response.choices[0].message.content}")
    message_history.append({"role":"assistant","content": response.choices[0].message.content})
  else:
    print("*"*50)
    print("*"*2," "*180, "감사합니다.", " "*17, "*"*2)
    print("*"*50)
    break
  # print(response.choices[0].message.content)
