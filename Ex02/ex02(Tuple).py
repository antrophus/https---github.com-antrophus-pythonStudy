print("========== tuple(튜플) ==========")
'''수정불가 특징이 있다: 수정하려면 리스트로 바꿔야 한다.'''
t = (1, 2, 3, 4) # tuple () vs  리스트 --> a = [1, 2, 3, 4]

print(type(t))      # type --> <class 'tuple'>

print(t[0], t[1], t[2], t[3])       # 1 2 3 4 : +index
print(t[-1], t[-2], t[-3], t[-4])   # 4 3 2 1 : -index

print(t[1:3])                       # (2, 3)    --> <class 'tuple'>
print(t[:])                         # (1, 2, 3, 4) --> <class 'tuple'>

print(t*2)                          # 원본은 수정되지 않음 (수정의 개념이 아님)
print(t)

print(t + (100, 200, 300))          # 원본은 수정되지 않음 (수정의 개념이 아님)
print(t)

print(len(t))                       # 개수 알아내기
print(3 in t)                       # 포함 여부 확인(튜플 안에 3이 있니?: True or False)

print("========== tuple(튜플) 생성 ==========")
t = (1, 2, 3, 4)        # 명확하게 튜플로 만들겠다고 표시.
tt = 100, 200, 300      # 변수 하나에 세 개의 값을 넣으면 기본값으로 튜플로 만든다.
print("tt의 타입: ",type(tt))

t = (99)                 # 값이 하나짜리 튜플 생성인지 연산을 위한 괄호 처리인지 알 수 없음. 값이 하나만 있을 때는 숫자임.
t = (99,)              # 값이 하나짜리 튜플 생성은 , 를 찍어야 함.
print("값이 하나짜리 튜플: ",t,type(t))

# 튜플의 형변환
a_list = list(t)
print(type(t))
print(type(a_list))