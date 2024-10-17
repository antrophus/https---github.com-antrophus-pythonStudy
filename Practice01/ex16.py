'''[ex16.py] 
주어진 문자열의 공백을 ','(콤마) 로 변경 후 출력하세요.
['T','h','i','s',' ','i','s',' ','a',' ','p','e','n','c','i','l']
'''
str = ['T','h','i','s',' ','i','s',' ','a',' ','p','e','n','c','i','l']

result = ''

for str2 in str:
    print(str2)
    if str2 == ' ':
        result += ','
    else:
        result += str2

print(result)