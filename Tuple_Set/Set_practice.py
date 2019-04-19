# 서로 다른 값을 가지는 집합(A, B)을 생성한다.
A = set((1, 3, 5, 7, 9, 11, 13))
B = set((2, 3, 5, 7, 11, 13))

# 집합(A, B)의 합집합, 교집합, 차집합 및 대칭차집합을 구한다
print("A와 B의 합집합 :", A | B)
print("A와 B의 합집합 :", A.union(B))
print("---------------------------------")
print("A와 B의 교집합 :", A & B)
print("A와 B의 교집합 :", A.intersection(B))
print("---------------------------------")
print("A와 B의 차집합 :", A - B)
print("A와 B의 차집합 :", A.difference(B))
print("---------------------------------")
print("A와 B의 대칭차집합 :", A ^ B)
print("A와 B의 대칭차집합 :", A.symmetric_difference(B))
print("---------------------------------")
###############################################################3
# 중복된 숫자정수)를 제거하는 함수를 만든다
def removeDuplicate(li):
    seen = set()			# 새로운 집합 변수 생성

    for item in li:
        seen.add(item)
    return list(sorted(seen))


li = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
print(removeDuplicate(li))
###############################################################
import re
# 리스트 정의
name_list = "김유덕, 이종표, 이재용, 박성호, 김성호, 최용수, 이성진, 박서영, 전경연, 송환수, 이재성, 김성호, 이성호, 박주상, 김성호"
# 리스트의 이름을 ','로 분리 및 변수 에 저장
split_result = name_list.split(', ')
# 특정 성씨를 가진 이름이 몇명 인지 찾을때 변수 생성 초기값 할등
countNum = 0
# 변수에 저장된 이름을 사용하여 for 문 실행
for num in split_result:
    # '김'으로 시작하는 이름 검색
    man = re.search('김.*', num)
    if man:
        countNum = countNum + 1

print("1) 15명의 명단 출력:", split_result)
print("\n2) 김씨는 모두 몇 명:", countNum)
print("\n3) \"김성호\"(이)란 이름은 몇 번 반복: ", split_result.count("김성호"))
result_List = list(set(split_result))
print("\n4 중복을 제거한 이름 출력: ", ", ".join(result_List))
result_List.sort()
print("\n5) 중복을 제거한 이름 오름차순 정렬 출력: ", ", " .join(result_List))

