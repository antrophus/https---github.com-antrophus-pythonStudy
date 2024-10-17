# 대입문(치환문)

a = 3
b = 5
c = a + b
print(a, b, c)

# 대입문 오류
# 1 + 3 = a

g, h, i  = 3.5, 5.3, 100

print(g, h, i)  

x=y=z=10

print(x, y, z)
# 자바와 달리 즉시 변경 가능
j= 3.5
k= 100
j, k = k, j
print(j, k)

# 같은 이름의 변수 사용가능
num = 1
print(type(num), num)

num = 'hello'
print(type(num), num)