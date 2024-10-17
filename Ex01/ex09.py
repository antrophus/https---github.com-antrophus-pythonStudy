# 문자열

s=""
str1 = "hello world"
str2 = "안녕 세상"

print(s, str1, str2)
print(type(s), type(str1), type(str2))
print(isinstance(str2, str))

#나는 "정우성"입니다.
str3 = '나는 "정우성"입니다.'
#str3 = "나는 \"정우성\" 입니다."
print(str3)

#나는 '박명수' 입니다.
str4 = "나는 '박명수' 입니다."
# str4 = '나는 \'박명수\' 입니다.'
print(str4)

print("================================")

s01 = "aaa"
s02 = "aaa"
print(s01,id(s01))
print(s02,id(s02))

s02 = "bbb"
print(s01, id(s01))
print(s02, id(s02))

#줄바꿈하고 싶으면 """ 을 씀 / 따옴표와 쌍따옴표도 자유롭게 쓸 수 있다.
str5 =   """ABCDEFG 
            abcdefg 
            가나다라마바사 
            123456789"""

print(str5)

#Hello World I'd say "Hello World"
print("Hello World I'd say \"Hello World\"") #"" 를 기본으로 사용
print('Hello World I\'d say "Hello World"') #'' 를 기본으로 사용

print("Hello\nworld I'd say \"hello world\"")

print("================================")

print("Hello!!!!!!!!!\rworld") # 현재 커서를 맨 앞으로 옮김
print("Hello\bworld")   # 현재 커서를 기준으로 백스페이스 (한칸 앞으로 이동)
print("hello\tworld") # 문자열 사이에 탭 간격(기본값:8칸)