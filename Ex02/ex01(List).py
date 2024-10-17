# list
print("===============List 기본===============")

test_list = [1, 12, 123, 1234]     

print(type(test_list))   # type ---> <class 'list'>

print(test_list[0], test_list[3])
print(test_list[-1])    # - 인덱스

print(test_list[1:3])   # 1번방 부터 ( 3 - 1)번 방까지 슬라이싱 문법 사용가낭

print(len(test_list))   # len() 메소드로 갯수 확인 : 파이썬의 기본 함수

print(test_list * 2)    # 곱하기 적용
print((test_list * 2)[5])   # 곱하기 적용 후에 방이 생김
print(test_list)        # 원본은 그대로

print(test_list + [100, 200, 300])

print(12 in test_list)

print("===============List 삭제===============")
# print(test_list)

# #del(test_list[0])
# del test_list[0]
print(test_list)

print("===============List 수정===============")

test_list[0] = "apple"
print(test_list)

b_list = ["apple", "banana", 10, 20]
b_list[2] =  b_list[2] + 90
print(b_list)

test_list = [1, 12, 123, 1234]
print(test_list[0:2])   # [1, 12] : 슬라이싱
test_list[0:2] = [888, 999]
print(test_list) #[888, 999, 123, 1234] : 원본이 바뀜

test_list[0:2] = [777]  # 두개의 방 0, 1 번방이 [777] 하나의 방으로 바뀜.
print(test_list)    # [888, 999] --> [777]

test_list[2:3] = [111] # = test_list[2] = 111
print(test_list)   

test_list[2:3] = ["aaa", "bbb", "ccc"] # 갯수가 맞지 않으면 늘리거나 줄여서 넣어줌
print(test_list)

print("===============List 슬라이스를 통한 삭제===============")
a = [1, 12, 123, 1234]

a[1:2] = [] # 1번째 방 삭제
print(a)
a[0:] = []
print(a)

print("===============List 슬라이스를 통한 삽입===============")
a = [1, 12, 123, 1234]

# a[1] = 'a'        #a[1:2] -> a[1] : 1번방 데이터를 수정

a[1:1] = 'a'        #a[1:1] -> a[1:0] : 1번방 자리에 추가
print(a)

a[5:] =[12345]      #5번 방을 만듬
print(a)

a[:0] = [-12, -1, 0]
print(a)

# 슬라이싱 문법 방번호 같으면 추가 [3:3]

print("===============List 메소드 사용===============")
a = [1, 12, 123, "hello", 3.14, 1000]

#추가

a.append("정우성") # 리스트의 맨뒤에 추가
print(a)

a.insert(2, "박명수") # 리스트의 중간에 지정한 자리에 추가
print(a)

a.extend([6,7,8])
print(a)

#삭제

a.remove(1000)      # 값으로 찾아서 삭제
print(a)

a.pop(6)           # 방번호로 삭제 del(a[6])
print(a)

a.pop()             # 방번호(x) --> 마지막 값 삭제
print(a)

print("===============List 메소드 사용(2)===============")

b = [1, 123, 1000, 12, 1000]
print(b)

#카운트
print(b.count(1000))    # 리스트에 1000 이 몇 개?

#뒤집기
b.reverse()             # 원본 리스트의 순서가 뒤집힘
print(b)

#정렬
b.sort()                # 원본 리스트가 오름차순 정렬
print(b)

b.sort(reverse=True)     # 원본 리스트가 내림차순 정렬
print(b)

#값으로 index 번호(방번호) 찾기
print(b.index(1000))    #처음 검색되는 방번호 리턴

b = [1, 123, 1000, 12, 1000]
for no in b:
    print(no)

print("------------------------")
