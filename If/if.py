#if문의 조건에 ()를 써도 되고 안써도 되는데 :은 꼭 써야한다
#들여쓰기로 서로 종속 관계를 따지니 주의해서 작성해야한다
#if 조건 : >> elif 조건 : >> else :
#조건은 참, 거짓으로 이루어진다 참일때 출력거짓일때 빠져나옴
#ex) while 문에서 ch = True 로 무한루프를 돌리다 ch = False로 해제가능함
#연산자 and or not 으로 bool 을 사용가능
#요소 in 튜플/리스트/문자열 있으면 true 없으면 false <> not in 을 쓰면 반대가된다
#제어문 조건을 정해서 나올수 있게하거나 어떠한 구문을 쓰면 나오게 할수있음
#이때 조건을 충족시키게 하거나 break 함수를 쓰는 경우가 있음
#contunue 는 반복문 맨처음으로 가게 하는 함수로 즉시 처음으로 가게됩(속한 반복문 맨처음)

A = [1, 2, 3, 4, 5, 6, 73, 8, 10, 54]
odd = 0
even = 0

for i in A:
    if i%2 == 1:
        odd += 1##
    elif i%2 == 0 :
        even += 1
print(odd, even )
