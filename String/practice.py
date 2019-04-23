# 연속된 긴 문자열을 입력 받은후 몇번 반복되는지 알아내라
string = 'abbcccddddeeeeeffffffggggghhhhhiiijjk'

# 변수(string)의 첫 번째 index의 값을 변수(result)에 할당
result = string[0]
count = 0

# 변수(sting)의 각 값들마다 for 문 실행
for st in string:
    # 만약 이전과 현재가 같은 문자이면:
    if st == result[-1]:
        count += 1		# 변수(count)의 값을 1씩 증가
    # 만약 이전과 현재가 다른 문자이면
    else:
        # 변수(count)의 값과 다음 문자를 변수(result)에 입력
        result += str(count) + st
        count = 1
result += str(count)

print(result)
###################################################################
A = 'abcdefghijklmnopqrstuvwxyz'


def itoa(s, num):		# 함수 정의

    # 만약 입력된 매개변수(num)이 공백과 같으면
    if num == '':
        print(s)
        return None
    else:
        print(int(num[0])-1)
        print(s)
    # 매개변수(s)의 값을 기존의 매개변수(s)에 매개변수
    # (num)의 숫자 값이 1자리인 문자와 나머지 한 자리
    # 숫자들로 구성된 문자들을 사용하여 자신의 함수 다시 호출
    itoa(s + A[int(num[0])-1], num[1:])

    # 만약 매개변수(num)의 길이가 2보다 크거나 같고
    # 매개변수(num[0:2])의 길이가 26보다 작거나 같으면
    if len(num) >= 2 and int(num[0:2]) <= 26:
        # 매개변수(s)의 값을 기존의 매개변수(s)에 매개변수
        # (num)의 숫자 값이 2자리 이상인 문자와 나머지
        # 한 자리 숫자들로 구성된 문자들을 사용하여
        # 자신의 함수 다시 호출
        print(int(num[0:2]))
        itoa(s + A[int(num[0:2])-1], num[2:])


it = input("숫자(정수) 입력 :")

# 매개변수로 공백과 키보드로부터 입력한 숫자(정수)를 사용하여 함수(itoa) 호출 및 실행
itoa('', it)
############################################################################
