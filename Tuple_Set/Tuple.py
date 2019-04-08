#종류		구성		타입
#문자열		문자		immutable
#리스트		요소		mutable
#딕셔너리	key:value		mutable
#튜플은 값을 바꿀수 없는 자료형이다
#다만 요소안 요소가 mutable이면 그 요소는 변경가능하다 튜플안 리스트에 리스트값을 바꿀순있다
#나머진 list와 같다


T1 = (1, 2, 3, 4, 5)
T2 = ("a", "b", "c", "d", "e")
T3 = ("A", "B", "C", "D", "E")

print(T1[2], T2[1])
print(T3[0:4])
print(T2 + T3)
print(T1 * 2)
