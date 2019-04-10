#반환값
#반환값에 맞게 함수를 호출하면서 같은 개수의 변수를 할당해야 한다
#반환값들을 하나의 리스트나 튜플로 묶으면 한개만 할당하면된다
#반환값들은 여려개일때 자동으로 튜플로 반환한다 리스트로 하고싶을경우 []를 써서 반환
#return 함수를 종료함과 동시에 값을 반환하는 키워드
#따라서 return이 연속적으로 있을경우 제일 먼저쓰여진 return을 읽음

def maxFunc(a):
    max = 0
    for i in a:
        if max < i:
            max = i
    return max

A = [1, 2, 3, 4, 5, 6, 73, 8, 10, 54]
maxNum = maxFunc(A)
print(maxNum)

