'''[ex15.py] 
5개의 숫자를 키보드로 입력받아 평균을 구하는 프로그램을 작성하세요.
'''
# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# num4 = int(input())
# num5 = int(input())

# average = (num1 + num2 + num3 + num4 + num5) / 5

# print(f"평균은 {average} 입니다.")


total = 0  
count = 0  

for i in range(5):
    num = int(input())
    total = total + num  
    count = count + 1    

average = total / count

print(f"평균은 {average} 입니다.")

