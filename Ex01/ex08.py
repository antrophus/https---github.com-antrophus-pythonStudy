# 확장 연산자

# str = ""
# str += "<table>"
# str += "</table>"
# print(str)
i = 0
i += 1  # i = i + 1
print(i)
x = 2
x = x + 2
print('x = ' , x)

x=3
x+=3
print(x)

x= 10

y=2
# y = y**2

y**=2
print(y)
print("--------------------")

a = 10
b = 20
c = a
d = 15-4
e = 11

print(id(a))
print(id(b))
print(id(c))
print(id(d))
print(id(e))
print("--------------------")
# 값 비교 == , 주소 값 비교 is
print(a == b) # 값이 같은가?
print(a is b) # 주소 값이 같은가?
print(a == c) # 값이 같은가?
print(a is c) # 주소 값이 같은가?

print(a == d) # 값이 같은가?
print(a is d) # 주소 값이 같은가?

print(d == e) # 값이 같은가?
print(d is e) # 값이 같은가?

# 논리 연산자 True or False
print("---------------------------")
print(True and True)   # True
print(True and False)  # False
print(False and True)  # False
print(False and False) # False

print(True or True)    # True
print(True or False)   # True
print(False or True)   # True
print(False or False)  # False

print(not True)     # False
print(not False)    # True


print("----------------------------------------")

#내장 수치 함수
print(abs(-3))            # 3  --> 절대값으로
print(abs(3))            # 3  --> 절대값으로
print(int(3.1415))       # 3  --> 정수형으로
print(float("3"))         # 3.0  --> 실수형으로
print(complex("3"))    # (3+0j)  -->복소수형으로
print(pow(2, 10))       # 2**10=1024   -->승수 계산

print("----------------------------------------")
print(complex("3")) # 3
