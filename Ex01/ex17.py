# num = input("숫자를 입력하세요")
# num = float(num)

# if num>0:
#     print("양수")
# elif num==0:
#     print("0")
# else:
#     print("음수")

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

# 문제 ifelse02.py
# 과목번호를 입력받아 강의실 번호를 출력하는 프로그램을 작성하세요
"""과목 code 값이 
    1이면 "R101호 입니다."
    2이면 "R202호 입니다."
    3이면 "R303호 입니다."
    4이면 "R404호 입니다."
    나머지는 "상담원에게 문의하세요"
    를 출력하세요"""

subject_code = int(input("과목번호를 입력하세요.\n"))

if subject_code == 1:
    print("R101호 입니다.")
elif subject_code == 2:
    print("R202호 입니다.")
elif subject_code == 3:
    print("R303호 입니다.")
elif subject_code == 4:
    print("R404호 입니다.")
else:
    print("상담원에게 문의하세요.")