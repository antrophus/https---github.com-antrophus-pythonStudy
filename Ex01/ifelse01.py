# 문제 ifelse01.py
# 숫자를 입력받아 아래와 같이 출력되는 프로그램을 작성하세요.
"""입력받은 수가 양수 일때, 짝수이면 "짝수" 출력 홀수이면 "홀수" 출력, 음수이면 "음수"라고 출력 0이면 "0"으로 출력"""

num = input("숫자를 입력하세요.\n")
float_num = float(num)

if float_num > 0:
    if float_num % 2 == 0:
        print("짝수")
    else:
        print("홀수")
elif float_num == 0:
    print("0")
else:
    print("음수")