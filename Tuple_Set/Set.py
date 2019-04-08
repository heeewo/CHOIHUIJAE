#set(값의 집합 자료형) 집합과 관련한 함수
#요소의 순서가 없다.
#중복되는 값은 한개만 저장한다
#딕셔너리는 key만 저장한다
#리스트는 저장안된다
#교집합 &, 합집합 |, 차집합 - 가된다
#s.add(a)		집합에 한 개의 값을 추가합니다.
#s.update([a,b,c...])	집합에 여러게의 값을 추가합니다.
#s.remove(a)	집합 s에 a를 삭제합니다.


S1 = {1, 3, 5, 7}
S2 = {5, 6, 7, 8, 9}

print(S1&S2, S1|S2, S1-S2, S2-S1)

S1.add("heeewo")

print(S1)
uplist = ["what", "the", 1, 3]
S2.update(uplist)
print(S2)
S2.remove(9)
print(S2)
