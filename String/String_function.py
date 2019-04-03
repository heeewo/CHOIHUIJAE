#count()		전달 인자의 문자 개수를 반환
#find()		함수의 대상이 되는 문자열에 전달 인자와 같은 문자가 있는지 찾고 그문자가 처음 발견된 인덱스 값을 반환. 만약 전달인자가 문자열 내에 없다면 -1 반환
#index()		파인드와 같은 역활, 전달 인자가 문자열 내에 없으면 오류 발생
#join()		전달 인자 사이에 함수의 대상이 되는 문자열을 삽입
#upper() /lower()	함수의 대상이 되는 문자열을 대문자로 / 소문자로 변환
#lstrip() /rstrip()	함수의 대상이 되는 문자열의 가장 왼쪽/오른쪽 공백을 모드 삭제
#strip()		함수의 대상이 되는 문자열의 양 쪽에 있는 한 칸 이상의 공백 모두 삭제
#replace()	replace(전달인자1, 전달인자2) 형식ㅇ로 사용하며,함수의 대상이 되는 문자열에서 전달인자1과 동일한 부분을 찾아 전달인자2로 바꿈
#split()		함수의 대상이 되는 문자열을 전달인자 기준으로 쪼개 리스트로 반환(ex. "g!oo!rm".split("!") > ['g','oo','rm']
#len()		문자열 길이
a = "Contrary to popular belief, Lorem Ipsum is not simply random text."

print(a.count('t'))

print(a.index('i'))

print(a.upper())

print(a.lower())

print(a.replace('a', 'b'))

print(a.split(" "))
