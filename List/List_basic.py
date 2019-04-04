#리스트안에는 어떠한 자료형도 다들어갈수 있다 리스트또한 말이다

my_list = ['a', 1, 2, 3, 'b', ['apple', 'banana'], 4]

print(my_list[3])
my_list[2] = "hello"
print(my_list[:])
print(my_list[0:6])
b = int(my_list[5].index('banana'))
print(my_list[5][b])			#안에 변수표현할때 포매팅안해도된다

#리스트안 리스트안의 내용은 인덱스를 어떻게 할까?