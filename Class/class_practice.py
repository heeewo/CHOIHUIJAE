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
# 직운 월급 인상률을 위한 클래스 정의
class Employee(object):

    # 월급의 인상률을 위한 변수 및 초기 값 설정
    raise_amount = 1.1

    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def apply_raise(self):
        self.pay = int(self.pay*Employee.raise_amount)


(name1, pay1) = input("이름과 월급(만원) 입력 :").split()
pay2 = int(pay1)
emp_1 = Employee(name1, pay2)
print(name1, "님의 기존 월급 :", emp_1.pay, "만원")
emp_1.apply_raise()
print(name1, "님의 인상 월급 :", emp_1.pay, "만원")
##################################################################
# 함수 pow(x, n) 만들기
class Py_solution:
    def pow(self, x, n):
        if x == 0 or x == 1 or n == 1:
            return x
        if x == -1:
            if n % 2 == 0:
                return 1
            else:
                return -1
        if n == 0:
            return 1
        if n < 0:
            return 1/self.pow(x, -n)

        val = self.pow(x, n//2)
        if n % 2 == 0:
            return val*val
        return val*val*x


(number1, number2) = input("pow(x, n) = x^n, a, b 입력 :").split()
num1 = int(number1)
num2 = int(number2)
py_solution = Py_solution()
print(num1, "^", num2, "=", py_solution.pow(num1, num2))
#########################################################################
# 시:분:초 형식의 전체 회수를 세기 위한 클래스 정의
class CountTime():
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '{0:02}:{1:02}:{2:02}'.format(self.hour, self.minute, self.second)

    def __add__(self, other):
        tempmin, self.second = divmod(self.second + other.second, 60)
        temphou, self.minute = divmod(self.minute + other.minute + tempmin, 60)
        self.hour = (self.hour + other.hour + temphour) % 24
        return self


count = 0
CountTime(0, 0, 0)

for hour in range(24):
    for minute in range(60):
        for second in range(60):
            time = CountTime(hour, minute, second)
            if '7' in str(time):
                count += 1

print(count, "번")
#############################################################################33
class Animal:
    def __init__(self, name):
        self.name = name

    def run(self):
        print("달려!")

    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("멍 멍!")


class Duck(Animal):
    def speak(self):
        print("꽥~꽥!")


dog = Dog("펑키")
n = dog.name
print(n + "야")

dog.run()
dog.speak()
############################################################

