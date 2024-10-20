
PI = 3.14

# 더하기 함수
def plus(a, b):
    return a + b

# 빼기 함수
def minus(a, b):
    return a - b

# 곱하기 함수
def multi(a, b):
    return a * b

# 나누기 함수
def div(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

# 원의 면적 구하기 함수
def area_circle(r):
    return PI*r**2

#직접실행 : 다른 파일에서 가져다 쓸 때 이 코든 실행이 안되고, 이 파일에서는 사용된다.
if __name__ == "__main__":
    print("====================================================")
    print(plus(55,66))
    print(area_circle(55))

#본인이 실행하면 --> __name__
#남이 부르면 --> 파일명