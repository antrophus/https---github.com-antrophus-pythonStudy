'''[ex12.py] 
사용자에게 연필의 개수와 인원수를 입력받아 모든인원에게 같은수의 연필을 나눠주려고 한다
1인당 연필의 받을수 있는 연필의 개수와 나머지를 구하시오'''

pencils = int(input('전체 연필갯수를 입력해주세요: '))
people = int(input('전체 인원수를 입력해주세요: '))

div = int(pencils/people)
rem = int(pencils%people)
print(f"1인당 연필의 갯수는 {div} 입니다.")
print(f"연필의 나머지 갯수는 {rem} 입니다.")