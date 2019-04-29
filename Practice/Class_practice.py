# 0~9사이 숫자를 가지고 숫자를 알아맞히는 게임
import random


class guess_number:
    def __init__(self, num):
        self.num = num

    def dice(self):
        self.dices = random.randint(0, 9)
        print(self.dices)

    def guess(self):
        self.dice()
        if self.num == self.dices:
            print("맞춤여 ㅊㅊ")
        else:
            print("틀림여 ㅋㅋ")


My_number = int(input("0~9까지 숫자를 입력하시오 :"))
Guess_number = guess_number(My_number)
Guess_number.guess()
#######################################################################

