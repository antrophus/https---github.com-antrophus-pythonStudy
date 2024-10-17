#복소수
a = 4 + 5j
print(a, type(a))           # (4+5j) complex
print(isinstance(a, complex)) # (4+5j) complex

b = 4 + 5j
c = 7 - 2j
print(b + c) # (11+3j)
print(type(b + c)) # (11+3j) complex
#실수부만 출력
print(b.real, b.imag) # 실수부, 허수부

################################
d = 5

#정수 --> 복소수 변환
print(d, type(d)) 
print(complex(d), type(complex(d)))

# 실수 --> 복소수
e = 7.5
print(e)
print(complex(e))

# 정수 --> 실수
print(float(d))

# 실수 --> 정수
print(int(e))

