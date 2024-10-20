'''<java에서의 함수 사용법>
public int plus(a, b){
    sum = a + b;
    return sum;
}
'''

'''<js에서의 함수 사용법> 
function plus(a, b){
    let sum = a + b;
    return sum;
}
'''
'''<js에서의 익명 함수>
let plus = function(){
    sum = a + b;
    return sum;
}
'''
'''<js 화살표 함수>
let plus = () =>{
    sum = a+b;
    return sum;
}'''

# python 에서의 lambda function

'''def 함수명(매개변수):
    (들여쓰기)  함수내용
    return 결과값'''
def plus(a, b):
    sum = a + b
    return sum

result = plus(5, 3)
print(result) 

def multiply(a, b):
    return a * b

result = multiply(7 , "하")

print(result)

print("================================================================")
#정의
def my_functions():
    print("hello function")
#실행
my_functions()

print("================================================================")
#내용이 없는 함수 표기법
#정의
def none_function():
    pass
#실행
none_function()

'''파이썬에서 내용이 없는 함수는 주로 "구현 예정" 또는 "구조를 미리 잡아놓기" 위한 용도로 사용됩니다. 
이는 프로그램의 큰 틀을 먼저 작성한 후 나중에 세부적인 코드를 채워 넣고자 할 때 유용합니다. 
이처럼 내용이 없는 함수는 pass 키워드를 사용하여 "아무것도 하지 않음"을 명시합니다.

pass는 파이썬에서 "빈" 코드 블록이 있어야 할 때 사용되는 예약어로, 에러 없이 해당 부분을 넘어갈 수 있게 해줍니다. 
예를 들어, 클래스나 함수의 구조는 만들어 놓았지만, 구현할 내용이 아직 없을 때 사용합니다.'''

print("================================================================")
# 1개 이상의 값을 return 할 수 있다.
#정의
def sum_and_mul(a, b):
    sum = a + b
    mul = a * b
    return sum, mul # 패킹

#언패킹 사용 안할 때
result = sum_and_mul(5, 3)
print(result)   # 튜플로 값이 나옴(5+3=8 , 5+3=15)
sum = result[0]
mul = result[1]
print("sum:", sum)
print("mul:", mul)

#언패킹
sum, mul = sum_and_mul(5, 3)
print(sum)
print(mul)

print("================================================================")

def plus_print(a=0, b=0):
    print(f"{a} + {b} = {a + b}")

plus_print(3, 5)    # a=3   b=5     #파라미터를 위치로 매칭
plus_print(3)       # a=3   b=0 
plus_print()        # a=0   b=0

print("================================================================")
#plus_print(,333)   # 오류
plus_print(b=333, a=2)   # 파라미터를 이름으로 매칭 / 이름을 알고 있기에 순서를 뒤섞어서 써도 된다.

print("================================================================")
'''
sum_many(1,2)
sum_many(1,2,3)
sum_many(1,2,3,4,5,6,7,8)
'''
#정의
'''
def sum_many(a,b):
    pass
def sum_many(a,b,c):
    pass
def sum_many(a,b,c,d,e,f,g,h):
    pass
'''

def sum_many(*a):
    print(type(a))

sum_many(1,2)
sum_many(1,2,3)
sum_many(1,2,3,4,5,6,7,8)

# 매개변수가 몇 개인지 정의 할 수 없을 때
# 정의
def sum_many(*args):
    for no in args:
        print(no)

    print("---------------")

sum_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

def sum_many(*args):
    sum = 0
    for no in args:
        sum += no
    print(sum)
    print("---------------")

sum_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
'''
def input_many(*num):
    sum = 0
    for no in num:
        sum += no
    print(sum)
    print("---------------")

a = int(input())
b = int(input())
c = int(input())
input_many(a,b,c)'''

print("================================================================")
# 모드 주구(고정값 하나) 다른 파라미터는 몇 개 인지 알 수 없음 
# 정의
def sum_mul(mode, *args):
    print("mode:", mode)
    if mode == "sum":
        result = 0
        for num in args:
            result += num
    elif mode == "mul":
        result = 1
        for num in args:
            result *= num
    else:
        print("mode를 입력해주세요")
    print(result)
    print("----------")
    

#사용
sum_mul("sum", 1,23,45)
sum_mul("mul", 1,23,45,22,2333)

print("================================================================")

def add_person(hp, **kwargs):
    print("hp:", hp)
    print("kwargs:", kwargs)
    print("----------")

add_person("010-1234-5678")
add_person("010-1234-5678", name="정우성")
add_person("010-1234-5678", name="정우성", age=20, conpany="02-1234-5678")
add_person("010-1234-5678", birth="2000-01-01", name="정우성", age=20, conpany="02-1234-5678")

print("================================================================")
print("============================mptitle==============================")
print("================================================================")

def add_person2(*hp, **kwargs):
    print(hp)            #폰번호 갯수 가변
    print(hp[0])

    print(kwargs)
    print(kwargs["name"])

    print("----------")

# add_person2("010-1234-5678")
# add_person2("010-1234-5678", "010-2345-6789")
add_person2("010-1234-5678", name="정우성")
add_person2("010-1234-5678", age=24, name="정우성")
add_person2("010-1234-5678", age=24, cname="(주)우리회사", name="정우성")