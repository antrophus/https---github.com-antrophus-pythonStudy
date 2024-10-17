'''[ex13.py] 
총급액을 입력하면 백원단위는 할인을 해주고 있습니다. 실제 지불금액을 출력하는 코드를 작성하세요
'''
total = int(input("전체금액을 입력해주세요: "))

str_total = str(total)      # int로 받은 입력값을 str로 변환
str_drop = str_total[-3:]   # 문자열 뒤에서 3번째까지의 값을 변수에 저장(100원단위 절사용)
drop = int(str_drop)        # 문자열 변환한 값을 int로 변환
print(f"실제 지불금액은 {total-drop} 입니다.")