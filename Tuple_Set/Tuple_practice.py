# 2명의 이름을 가진 Tuple에서 꺼내오기

for name in ('John', 'Kate'):
    print("hello", name, "sina 빰빰빠라빰")
##########################################################
# 키보드로부터 Tuple들의 목록을 입력받은 후 문자 하나하나를 분리하여 오름차순 순서대로 프로그램


def last(n):
    return n[-1]


def sort(tuples):
    return sorted(tuples, key=last)


# 키보드로부터 Tuple들의 목록 입력
tup = input("Enter a list of tuples :")
print("Sorted : ", sort(tup))
############################################################
# 내가 가진 애완견 이름 3개로 구성된 Tuple을 성정하고 변수 에 저장
myPet = ('파이썬', '백구', '오라클')
# 키보드로부터 애완견 이름을 입력받아 새로운 변수에 저장
name = input("애완견의 이름을 입력 :")
# 키보드로부터 입력된 애완견 이름을 가진 변수가 있는지 확인
if name not in myPet:
    print("나의 애완견이 아니다")
else:
    print("입력된 애완견은 나의 애완견이다")
##########################################################
