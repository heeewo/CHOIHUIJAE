#딕셔너리는 인덱스 순서가 필요없다. key: value형태로 저장 한다 
#입력방법은 이름 = {"~~" : "~~" , "~~" :"~~"} or 이름 = diction( ~~ = "~~" ~~~)
#리스트와 다르게 비어있어도 그냥 추가 가 가능 dic['~']=~~형식으로 추가
#del 명령어로 삭제 가능
#주의점	1. key는 value를 찾기 위한 유일한 값이기 때문에 중복 사용 불가
#	2. key에 리스트는 사용할수 없습니다.
#	3. value에는 어떤 값이던 상관 없이 올 수 있습니다.

phones = {"medel" : "iphoneXS", "manufacturer" : "apple", "year" : "2018"}
print(phones)
del phones["year"]
print(phones)
