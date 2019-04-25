PI = 3.14159


class Circle:
    def __init__(self, radius):			 # 생성자
        self.radius = radius

    def Area(self, radius):
        self.radius = radius
        area = PI*self.radius*self.radius
        return area

    def Circum(self, radius):
        self.radius = radius
        circumference = 2.0*PI*self.radius
        return circumference


radius = float(input("원의 반지름 입력:"))
circle = Circle(radius)
print("원의 면적 :", circle.Area(radius))
print("원의 둘레 :", circle.Circum(radius))
#################################################################
# 로또 번호를 자동으로 생성하여 출려하는 프로그램
import random


class LottoBall:
    def __init__(self, num):
        self.num = num


class LottoMachine:
    def __init__(self):
        self.ballList = []
        for i in range(1, 46):
            self.ballList.append(LottoBall(i))

    def selectBalls(self):
        random.shuffle(self.ballList)
        return self.ballList[0:6]


class LottoUI:
    def __init__(self):
        self.machine = LottoMachine()

    def playLotto(self):
        input("로또 번호 뽑기(Enter)")
        selectedBalls = self.machine.selectBalls()
        for ball in selectedBalls:
            print("%d" % (ball.num))


ui = LottoUI()
ui.playLotto()
###################################################################

