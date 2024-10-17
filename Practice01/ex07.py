'''[ex07.py] 
사용자로부터 가로 세로 값을 입력받아 삼각형의 넓이를 구하는 프로그램을 작성하세요
'''

width = float(input("가로: "))
height = float(input("세로: "))

area = (width * height) / 2
print(f"삼각형의 넓이는 {area} 입니다. ")