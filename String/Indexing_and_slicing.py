# ord("A") 문자를 아스킵코드로 chr(65)아스킵코드를 문자로
# 문자열 자료형은 Innutable 타입으로 한번 초기화하면 사용자임의로 값을 바꿀수 없다(함수 써야한다)
a = "goorm can make rainbow with best environment"
b = a[1]+a[-9]+a[-3]+a[-7]+a[5]+a[25:27]+a[-3]+a[5]+a[15:22]
print(b)
