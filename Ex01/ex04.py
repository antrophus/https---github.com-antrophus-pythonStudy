# 정수형
a = 101
print (a, type(a))
print(isinstance(a, int))


# 2진수 기호 : 0b
b = 0b10
print (b, type(b))

# 8진수 기호 : 0o
c = 0o10
print (c, type(c))

# 16진수 기호 : 0x10
d = 0x19
print (d, type(d))

#10진수 -> 2진수, 8진수, 16진수로 표현
print (bin(5)) #10진수 '5'의 '2진수' 표현 : 0b101

print (oct(65)) #10진수 '65'의 '8진수' 표현 : 0o101

print (hex(257)) #10진수 '257'의 '16진수' 표현 : 0x101

#큰수(지수)
e = 2**1024
print(e, type(e))