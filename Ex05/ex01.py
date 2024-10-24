'''
1. 최소 버전 + 토큰값
'''

import os         # os 모듈을 사용해서 환경변수에 접근
from openai import OpenAI

openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key = openai_api_key)

response = client.chat.completions.create(
  model="gpt-3.5-turbo-0125",
  messages=[
    {"role":"system","content":"너는 일반적인 문장을 시로 표현을 잘하는 재능을 가진 유명한 시인이야. sns와 인터넷에서 유행하는 밈을 잘 활용해서 시를 창작하고 있어."},
    {"role":"user","content": input("시적인 표현을 원하는 당신만의 주제를 알려주세요: ")}
    ],
  temperature=0.7,
  max_tokens=2048,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  response_format={
    "type": "text"
  }
)

print(response.choices[0].message.content)

# 토큰 수 확인
q_token = response.usage.prompt_tokens      #질문 토큰수
a_token = response.usage.completion_tokens  #응답 토큰수
t_token = response.usage.total_tokens       #전체 토큰수
print(f"질문 : {q_token} + 응답 : {a_token} = 합계 : {t_token}")
