print("========== dictionary(딕셔너리) ==========")

a = {}      #생성방법 / list [] : tuple () : dictionary {}

#추가
# key : value
# "R38" "빅데이터반"
a["R38"] = "빅데이터반"
a["R32"] = "풀스택반"
print(a)

# 생성 방법
d = {"basketball": 5, "soccer": 11, "baseball": 9}
print(d)
#추가
d["volleyball"] = 6
print(d)

# 값 출력
print('d 딕셔너리의 basketball의 값 출력 방법(1): d["basketball"] = ', d["basketball"])
print('d 딕셔너리의 basketball의 값 출력 방법(2): d.get("basketball") = ', d.get("basketball"))

# 값 삭제
print("=====딕셔너리 값 삭제=====")
d = {"basketball": 5, "soccer": 11, "baseball": 9}
print(d)
print()
print('삭제방법(1):1개 값 삭제 = ','del(d["soccer"])')

del(d["soccer"]) # 1개 값 삭제

print(d)
print()
d = {"basketball": 5, "soccer": 11, "baseball": 9}
print('삭제방법(2):전체삭제(1) = ','d ={}')

d ={} # 전체삭제(1)

print(d)
print()
d = {"basketball": 5, "soccer": 11, "baseball": 9}
print('삭제방법(3):전체삭제(2) = ','d.clear()')

d.clear() # 전체삭제(2)

print(d)
print(type(d))

print("==============찾기==============")
# 찾기
d = {"basketball": 5, "soccer": 11, "baseball": 9}
print(d)
print(len(d), "개")
print("soccer" in d, " :soccer 가 딕셔너리에 있니? True or False")
print("soccer" not in d, " :soccer 가 딕셔너리에 없니? True or False")


print("==============딕셔너리의 키들을 리스트로 반환==============")
d = {"basketball": 5, "soccer": 11, "baseball": 9}
keys = d.keys()
print(keys, type(keys))

for key in keys:
    print(key)
    print(d[key])
    #print(f"{key} -> {d[key]}")
    
print("==============딕셔너리의 값 을 리스트로 반환==============")
value_list = d.values()
print(value_list, type(value_list))

for value in value_list:
    print(value)

play_list = d.items()
print(play_list, type(play_list))

t = ("apple", "banana", 10, 20)
for item in t:
    print(item)

print("-----------------------")
for index, item in enumerate(t):
    print(index, item)

