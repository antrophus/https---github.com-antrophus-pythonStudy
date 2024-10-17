# 스위치 케이스문

code = int(input("과목번호를 입력해주세요\n"))

match code:
    case 1:
        print("R101호 입니다.")
    case 2:
        print("R202호 입니다.")
    case 3:
        print("R303호 입니다.")
    case 4:
        print("R404호 입니다.")
    case _:
        print("상담원에게 문의하세요")