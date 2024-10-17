'''[ex18.py] 
1~45까지의 숫자 중 임의의 6개의 숫자를 출력하세요-미니로또
랜덤함수 검색해볼것
중복체크 할 것
'''
# 랜덤함수
import random

# len
numbers = set()

while len(numbers) < 6:
    numbers.add(random.randint(1, 45))
print("미니로또: ", numbers)

print("======================================")

# range
numbers = random.sample(range(1, 46), 6)

print("미니 로또: ", numbers)