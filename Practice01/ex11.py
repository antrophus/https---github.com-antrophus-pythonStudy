'''[ex11.py] 
동전별 개수를 입력받아 총금액을 계산하는 프로그램을 작성하세요. 
'''
obac = int(input("500원의 개수: "))
bac = int(input("100원의 개수: "))
osip = int(input("50원의 개수: "))
sip = int(input("10원의 개수: "))
print(f"동전의 총합은 {obac*500 + bac*100 + osip*50 + sip*10} 원 입니다.")