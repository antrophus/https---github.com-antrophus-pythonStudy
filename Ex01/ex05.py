# 실수형

a  = 1.2
print(a, type(a))           # 1.2 float
print(isinstance(a, float)) # True
print(isinstance(a, int))   # False
print(a.is_integer())       # False

# 큰 수 표현
b = 1.0e5
print(b, type(b))           # 100000.0 float
b = 1.0E5   
print(b, isinstance(b, float))  # 100000.0 True

# 작은 수 표현

c = 1.0e-2
print(c, type(c))           # 0.01 float
c = 1.0E-2
print(c, isinstance(c, float))  # 0.01 True

# 예제
d = 3e3 #3.0*10의 3승
print(d, type(d))       # 3000.0  float

e = -0.2e-4 
print(e, type(e)) 


