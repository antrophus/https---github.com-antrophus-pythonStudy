'''[ex09.py] 
[문제] Ex18 사용자로부터 화씨 온도를 입력받아 섭씨 온도로 변환하는 프로그램을 작성하세요.
*[참고] ℃ : 섭씨 기호   ℉ : 화씨 기호
화씨🡪섭씨 ℃ = 5/9 * (℉ - 32)           섭씨🡪화씨 ℉ = (℃ * 9/5) + 32
'''

Fahrenheit = float(input("화씨: "))
Celsius = 5/9*(Fahrenheit - 32)
print(f"화씨 {Fahrenheit} 의 섭씨온도는 {Celsius} 입니다.")