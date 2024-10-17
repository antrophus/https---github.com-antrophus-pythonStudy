# 문자열의 연산

str1 = "FirstString"
str2 = "SecondString"

print(str1 + str2) # FirstStringSecondString

print(str1*3) # FirstStringFirstStringFirstString

print("=" * 50) 
print("My Program") 
print("=" * 50)

print("----------------------------------------")

# 문자열의 indexing

str1 = "First String"
# , 와 + 의 차이
print(str1[0], str1[1], str1[4]) # F i t 데이터 3개 : ,
print(str1[0] + str1[1] + str1[4]) # Fit 데이터 1개 : +

# 맨 끝의 문자를 뽑고 싶을 때
print(str1[11]) # 마지막 글자의 번호를 앞에서 부터 찾아서 넣음
print(str1[-1]) # 마지막 글자의 번호를 뒤에서 부터 불러올 수 있다.

# 맨 앞의 문자를 뽑고 싶을 때
print(str1[-12]) # 마지막에서부터 세어서 거꾸로 번호를 매겨서 씀
print(str1[0]) # 처음의 번호

print("----------------------------------------")
# F r _ S g 를 마지막 글자에서 부터 찾아서 출력해보자

print(str1[-12], str1[-4], str1[-7], str1[-6], str1[-1])
print(id(str1[2]))
print(id(str1[8]))

print("----------------------------------------")

# 문자열의 슬라이싱
print(str1[0] + str1[1] + str1[2] + str1[3] + str1[4])
print(str1[0:5]) # 0번부터 5번 '앞'까지(첫글자부터 여섯번째 글자의 바로 앞까지) = str1[0] + str1[1] + str1[2] + str1[3] + str1[4]
print(str1[:5]) # 처음 부터 시작할 경우 '0'은 생략할 수 있다. *많이 쓰임.

print("===============================================================")
print(str1[1:9:3])  # 두번째 글자부터 8번째 글자까지 3칸씩 건너뛰면서 출력
print(str1[3:])     # 4번째 글자부터 마지막 글자까지
print(str1[:])
print(str1[-6:-2])
print(str1[::-1]) # 마지막부터 처음으로 배열을 뒤집어서 출력

# str1[5]= "a" : 이미 확정된 문자열의 중간 값만 변경할 수는 없다. : 문자열을 전부 변경하는건 가능
print(str1)
print("===============================================================")
name = "이효리"
name2 = name[::-1]
print(name)
print(name2)
print(name == name2) #False

name = "토마토"
name2 = name[::-1]
print(name == name2) #True
