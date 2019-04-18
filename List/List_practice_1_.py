# 1부터 10까지 숫자들 중에서 첫 번째 3개의 숫자(1, 2, 3)를 제외하고 나머지 숫자들의 제곱의값을 구하여 리스트로 출력
# 리스트 변수 생성


def squareValues():
    li = list()
    for i in range(10):
        li.append(i**2)

    print(li[3:])


squareValues()
###########################################################################
# 주어진 문자열들의 리스트(list)에서 처음과 마지막 문자가 같고
# 문자열의 길이가 2보다 크거나 같은 문자열들을 찾아
# 개수와 함께 출력하는 프로그램을 작성하시오
# for문속 문자열을 받아올때 그 문자열도 리스트형식으로 바뀜을 알수있다

def match_words(words):
    num = 0					# 일치하는 단어갯수
    li = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            num += 1		# 변수에 단어 개수 추가
            li.append(word)

    print(li, "=>", num, "개")


mwords = ['abc', 'xyz', 'aba', '1221']
print("첫 문자와 마지막 문자가 같은 단어: ")
match_words(mwords)
###########################################################################
# 행운의 메세지를 전달
import random
dimention2_list = [['항상', '오늘 하루도', '올 한해에도'], ['건강', '행복', '사랑'], '하세요']


print("당신을 위한 행운의 메시지 전달 시스템입니다.")
while(1):
# 행운의 메세지를 전달
import random
dimention2_list = [['항상', '오늘 하루도', '올 한해에도'], ['건강', '행복', '사랑'], '하세요']


print("당신을 위한 행운의 메시지 전달 시스템입니다.")
while(1):
    A = input("행운의 메시지를 받아보시겠습니까? (Y/N)")
    if A == 'y' or A == 'Y':
        print(dimention2_list[0][random.randint(0, 2)], dimention2_list[1][random.randint(0, 2)], dimention2_list[2])
        break
    else:
        print("행운의 메시지를 받을수 밖에 없어요")

