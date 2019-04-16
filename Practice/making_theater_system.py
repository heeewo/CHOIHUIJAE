movies = ["Batman", "Harry Porter", "Scream", "Happy Dog"]
print("관람하실 영화를 입력해 주세요.")
for movie in movies:
	print(movie)

print("관람하실 영화를 입력해 주세요.")
choice = input()


while choice not in movies:
	print("다시 선택해 주세요.")
	choice = input()
	

print("관람하실 인원을 입력해 주세요.")
number = int(input())


while not((type(number)==int) & (number > 0)):
	print("인원은 양수이고 정수이어야 합니다.")
	number = int(input())
	

print("할인권이 있는 경우 y 입력, 없는 경우 n 을 입력해 주세요.")


coupon = input()


coupon_price = 0


if coupon == 'y':
	print("할인권의 금액:")
	coupon_price = int(input())


original_price = 12000


price_sum = original_price * number - coupon_price


print("영화이름 : %s" %choice)
print("결제 내역")
print("영화 좌석 가격 : %d" %original_price)
print("인원: %d" %number)
print("할인 금액 : %d" %coupon_price)
print("최종 금액 : %d" %price_sum)
