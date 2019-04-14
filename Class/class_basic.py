#객체를 생성한 클래스와의 관계를 얘기하면 '인스턴스'라고 한다
#붕어빵 틀 :
#       속재료, 밀가루 반죽
#       구운 시간
#       기능 붕어빵 굽기 :
#           속 재료, 밀가루 반죽, 구운 시간을 가지고 만들기
#           return 어떤붕어빵
#class Triangle :           #클래스선언
#   pass                    #실행할 내용이 없을때 지나치라는 명시적
#tri1 = Triangle()          #객체이름 = 클래서() 선언
#
#class Triangle :
#   def setData(self, b, h) :
#       self.b = b
#       self.h = h
#tri1 = Triangle()          #객체 생성
#tri1.setData(4, 5)         #객체 메소드 실행
#print(tri1.b, tri1.h)
#클래스 내에 메소드는 def setData(self, b, h) :와 같이 일반 함수와 같은형식 선언
#객에는 객체이름.메소드(전달인자)형식
#self 매개변수 self는 객체 tri1을 전달 받는다는 뜻입니다.
#self.b = b형식은 tri1.b = b와 같고 '객체 tri1필드 b에 전달받은 b를 저장'
#   def area(self) :        #def area() :불가능
#       return self.b * self,h /2 
# 함수 : 특정 기능 집합 >>> 메소드 : 클래스안의 함수  >>> 생성자:객체 생성 자동호출
# 생성자는 _init_이라는 이름을 사용해야합니다.
# tri1 = Triangle(4, 5)     #이런 식으로 바로 생성가능
# def __init__(self, b, h = 5)  #이런식으로 고정값을 정할수도 있다 자동생성


