# 출력 : java의 println
# ,는 공백으로 표시된다.
print("orange" "banan" "apple") 
print("orange"+"banan"+"apple")
print("orange","banan","apple")

# sep= 출력할 때 구별하는 기준을 출력 기본값은 " " :공백.
print("orange", "banan", "apple", sep=",") #: 여기서는 콤마(,)를 출력
print("orange", "banan", "apple", sep="***") #: 여기서는 별(***)를 출력
print("orange", "banan", "apple", sep="__") #: 여기서는 언더바(__)를 출력

# 마지막 문자열을 지정할 수 있으며 기본값은 "\n" :줄바꿈. 
print("orange", "banan", "apple", end="=====\n") 
print("orange", "banan", "apple", end="\n") 


# 구분자와 마지막 값을 같이 쓸때
print("orange", "banan", "apple", sep=",", end="======") # 콤마를 구분자로 쓰고, 끝을 지정한 값으로 마무리