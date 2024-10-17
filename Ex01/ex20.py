animal_list = ["cat", "cow", "tiger"]

for animal in animal_list:
    print(animal)
    print("-----")

"""
range() 함수 : for 문에 많이 쓰임

range(시작, 끝, 증가값)
range(시작, 끝)
range(끝)

"""
print("================================================")
print("0부터 9까지")
for no in range(0,10):
    print(no)

print("================================================")
print("5부터 9까지")
for no in range(5,10):
    print(no)

print("================================================")
print("0부터 9까지 3개씩")
for no in range(0,10,3):
    print(no)
print()
"""[예제 for03.py]
아래와 같이 출력하는 프로그램을 작성하세요
0 2 4 6 8
"""
print("아래와 같이 출력하는 프로그램을 작성하세요: 0 2 4 6 8")
for no in range(0, 10, 2):
    print(no, end=" ")
print("\n\n")

"""[예제 for03.py]
아래와 같이 출력하는 프로그램을 작성하세요
5 4 3 2 1 0 -1 -2 -3 -4 -5
"""
print("아래와 같이 출력하는 프로그램을 작성하세요: 5 4 3 2 1 0 -1 -2 -3 -4 -5")
for no in range(5, -6, -1):
    print(no, end=" ")
print("\n\n")

"""[문제 for04.py]
숫자를 입력받아 입력한 숫자(단)의 
구구단을 출력하세요 (for문으로작성)
"""
print("================================")
print("----------구구단 전체----------")
for i in range(2, 10, 1):
    print(f"{i}단:")
    for j in range(1, 10, 1):
        print(f"{i} * {j} = {i*j}")
    print()
print("================================")
print("구구단")
number = int(input("단을 입력하세요: "))

for i in range(1, 10, 1):
    print(f"{number} * {i} = {number*i}")

print("\n\n")


