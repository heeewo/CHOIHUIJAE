# 임의의 숫자를 생성하기 위한 라이브러리 호출
import random
# 변수 생성 및 초기 값 할당
min = 48
max = 122
passwd = []
# 비밀번호는 6자리로 되어야함 반복
# 알파벳 대문자, 소문자, 숫자 및 특수 문자 rand함수 사용 아스킵코드 변환
for i in range(6):
	passwd.append(chr(random.randint(min, max)))
# 비밀번호를 한 개를 자동 생성
# 비밀번호를 출력
print(passwd)
#########################################################################
import math
# 함수 생성


def Sphere_Volume(r):
	return 4/3*3.14*r**3


# 서로 다른 크기의 원구와 같은 풍선 생성 반지름 (r)을 입력받음
sue = int(input("철수의 풍선 반지름을 입력하시오 :"))
hae = int(input("영희의 풍선 반지름을 입력하시오 :"))
# 부피 비교
if Sphere_Volume(sue) > Sphere_Volume(hae):
	print("철수 풍선이 더 큽니다")
elif Sphere_Volume(sue) < Sphere_Volume(hae):
	print("영희 풍선이 더 큽니다")
else:
	print("풍선크기가 같습니다")
###########################################################################
class Phonebook():
    phone_book = dict()
# 새로운 전화번호 추가

    def SetPhone(self):
        a = input("이름을 입력하시오 :")
        b = input("번호를 입력하시오 :")
        self.phone_book[a] = b

# 전체 전화번호 목록
    def GetPhone(self):
        print(self.phone_book)

# 전화 번호 삭제
    def RemovePhone(self):
        c = input("삭제할 이름을 입력하시오 :")
        del self.phone_book[c]

# 이름 수정
    def ModifyPhone(self):
        print(self.phone_book.keys())
        d = input("수정될 이름을 입력하시오 :")
        e = input("수정할 이름을 입력하시오 :")
        self.phone_book[e] = self.phone_book[d]
        del self.phone_book[d]


My_Phone = Phonebook()
while(1):
    print("실행할 명령을 입력하세요\n1 : 전체 전화번호 목록")
    A = input("2 : 전화번호 새로추가\n3 : 전화 번호 삭제\n4 : 이름 수정\n5 : 종료\n")
    if A == '1':
        My_Phone.GetPhone()
    elif A == '2':
        My_Phone.SetPhone()
    elif A == '3':
        My_Phone.RemovePhone()
    elif A == '4':
        My_Phone.ModifyPhone()
    elif A == '5':
        break
    else:
        pass
#######################################################################33
# BMI 인자들을 입력받고
# BMI 값들을 계산


def BMI():
    a = int(input("체중 :"))
    b = int(input("키 :"))
    return a/b**2


def Bodyshape():
    A = BMI()
    if A < 18.5:
        print("마른체형")
    elif 18.5 <= A < 25:
        print("표준")
    elif 25 <= A < 30:
        print("비만")
    else:
        print("고도비만")


Bodyshape()
