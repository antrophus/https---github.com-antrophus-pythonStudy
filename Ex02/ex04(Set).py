print("========Set===========")

print("set 만들기====================")
no_list={1,2,3}
print(no_list, type(no_list))
#길이(size, 몇 개)
print(len(no_list))
#포함 값 찾기
print(2 in no_list)
print(2 not in no_list)

print("set 메소드====================")
print("추가: .add(100)")
#추가
no_list.add(100)
print(no_list)
print("================")

print("삭제: .discard(500) 해당 값 없을 경우 변화 없음")
no_list.discard(500)
print("discard: ", no_list)
print("================")

print("삭제: .remove(100) 해당 값 없을 경우 에러")
no_list.remove(100)
print("remove: ",no_list)
print("================")

print("수정: .update({2, 3}) 수정")
no_list.update({5, 6})
print("update: ",no_list)
print("================")

print("삭제: .clear() 전부 비움")
no_list.clear()
print("clear: ",no_list)

print("======== > 집합 < ===========")
s1 = {1,2,3,4,5,6,7,10}
s2 = {10, 20, 30}
print(type(s1), type(s2))

s3 = s1.union(s2)   #합집합
s3 = s1 | s2
print("s3(합집합): ",s3)
'''
print("합집합: s1 | s2 = ", s1 | s2)
print("합집합: |s1| |s2| = ", len(s1) | len(s2))
'''

s4 = s1.intersection(s2) # 교집합
s4 = s1 & s2
print("s4(교집합):", s4)

s5 = s1.difference(s2)  # 차집합
s5 = s1 - s2
print("s5(차집합)s1 - s2:", s5)

s6 = s2 - s1
print("s6(차집합)s2 - s1: ", s6)