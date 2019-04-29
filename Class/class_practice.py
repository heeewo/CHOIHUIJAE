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
# 성명, 나이, 성별, 월급 및 입사일 등을 입력받아 각 항목에 맞게 출력하는 프로그램
class Person:
    def __init__(self, name, age, gender):
        self.Name = name
        self.Age = age
        self.Gender = gender

    def aboutMe(self):
        print("이 름 : " + self.Name)
        print("나 이 : " + self.Age)
        print("성 별 : " + self.Gender)


class Employee(Person):
    def __init__(self, name, age, gender, salary, hiredate):
        Person.__init__(self, name, age, gender)
        self.Salary = salary
        self.Hiredate = hiredate

    def aboutMe(self):
        Person.aboutMe(self)
        print("월 급 : " + self.Salary + "원")
        print("입사일 : " + self.Hiredate)


oEmployee = Employee("김선우", "20", "남", "2,000,000", "2027년 10월 20일")
oEmployee.aboutMe()
########################################################################
# 다각형을 만드는 다각형 클래스를 생성 상속으로 삼각형 클래스를 선분의 길이를 차례대로 입력받은 후 삼각형의 넓이를 구하여 출력
class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = no_of_sides

    def inputSides(self):
        self.sides = [float(input("선분" + str(i+1) + "의 길이 입력 :"))for i in range(self.n)]


class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)

    def findArea(self):
        a, b, c = self.sides
        s = (a + b + c)/2
        print('Semi-permimeter = (' + str(a) + '+' + str(b) + '+' + str(c) + ') /2 =' + str(a+b+c)+ '/2 =', s)
        area = (s*(s-a)*(s-b)*(s-c))**0.5
        print('삼각형의 면적 : %0.2f' % area)


tri = Triangle()
tri.inputSides()
tri.findArea()
######################################################################3`
