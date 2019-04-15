#'인스턴스 번수'는 각 객체의 고유 값이라 다른 객체와 공유하지 않습니다.
#같은 클래스로 만들어진 인스턴스끼리 공유하고 접근이 가능한 '클랜스 변수'
#class Triangle :
#       cal_count = 0       #클래스 안에서 변수 지정
#   def area(self) :
#       Triangle.cal_count += 1     #인스턴스 끼리 공유가 되기때문에
#       return self.b * self.h /2   #tri1.cal_count도 가능하다
#'인스턴스 메소드'는 self를 사용해 인스터스의 필드에 접근하는 메소드
#self매개변수를 가지지 않는 메소드를 '정적 메소드'라고 한다 
#클래스 안에서 선언되고 인스턴스로 실행하지만 필드를 접근하지 않아 함수같이 사용
#메소드 선언 앞에 @satticmethod 라고 표시해야 정적 메소드로 인식한다.
#인스턴스의 필드에 접근할 수 없어서 영향을 줄수 없기 때문에 tri1.~~ Triangel.~~둘다 사용가능
#정적 메소드에서 클래스 변수를 사용할려면 클래스 메소드를 사용
#@classmethod라고 표시하면 사용 가능 'self'처럼 'cls'를 관용적으로 사용

