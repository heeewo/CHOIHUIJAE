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
# 커피 자판기 만들기
class AutoMachine:
    def insert_coin(self, coin):
        self.coin = coin

    # 1,000원이상일시 커피 몇잔이 필요한지 경우
    def give_coffee(self):
        self.num = int(input("몇 잔을 원하세요 (" + str(self.coin//500) + "가능) :"))

    def give_receipt(self):
        print('입금 금액 :', self.coin, '원 ' '커피 :', self.num, "잔")

    def Auto(self, coin):
        self.insert_coin(coin)
        self.give_coffee()
        self.give_receipt()


# 금액이 초과한 경우 반환
class excess_coin(AutoMachine):
    def insert_coin(self, coin):
        AutoMachine.insert_coin(self, coin)

    def give_coffee(self):
        AutoMachine.give_coffee(self)
        self.exchange = self.coin
        self.exchange -= self.num*500

    def give_receipt(self):
        AutoMachine.give_receipt(self)
        print("잔돈 :", self.exchange, "원")


# 금액이 부족한경우 메세지 출력
class less_coin(excess_coin):
    def insert_coin(self, coin):
        excess_coin.insert_coin(self, coin)

    def give_coffee(self):
        excess_coin.give_coffee(self)
        self.morecoin = 500 - self.coin
        print(self.morecoin, "원 만큼 더필요합니다")

    def give_receipt(self):
        excess_coin.give_receipt(self)

    def Auto(self, coin):
        self.insert_coin(coin)
        self.give_coffee()
        self.coin += int(input("현금을 더 추가하세요(반환 = 0) :"))
        if self.coin >= 500:
            excess_coin.give_coffee(self)
        self.give_receipt()


coin = int(input("현금을 입금하세요"))
if coin > 500:
    autoMachine_on = excess_coin()
elif coin == 500:
    autoMachine_on = AutoMachine()
else:
    autoMachine_on = less_coin()
autoMachine_on.Auto(coin)
##############################################################################
import random


class guess_number:
    def __init__(self, num):
        self.num = num

    def dice(self):
        self.dices = random.choice([2, 0, 5])
        RCP = {2: '가위', 0: '바위', 5: '보'}
        print(RCP[self.dices])

    def guess(self):
        self.dice()
        compare = self.num - self.dices
        if compare < 0:
            if abs(compare) <= 3:
                print("이김여 ㅊㅊ")
            else:
                print("짐여 ㅋㅋ")
        elif compare > 0:
            if compare == 5:
                print("이김여 ㅊㅊ")
            else:
                print("짐여 ㅋㅋ")
        else:
            print("비김 ㅎㅎ")


while(1):
    My_number = int(input("가위(2) 바위(0) 보(5) 그만(1):"))
    if My_number == 1:
        break
    Guess_number = guess_number(My_number)
    Guess_number.guess()

