#a=f.readline() : 파일 객체 f의 첫번째 줄을 읽고 a에 반환합니다. 만약 파일을 닫지 않으면 이 함수를 실행할 때마다 한줄씩 읽어들입니다.
#a=f.readlines() : 파일 객체f의 모든 줄을 읽고 각 줄을 리스트 형식으로 a에 반환합니다
#a=f.read() : 파일 객체 f의 모든 문자열을 읽고 a에 반환합니다.
#파일의 행수를 알수있다면 for문 모르겠다면 while문에 break를 넣어준다
#ex) if not line(변수a) : bread #line이 None이 되면 즉 false가 되면 반복문 탈출

F = open('data/unsort.txt','r')

A = F.read().split('\n');A.remove('')
A = list(map(int,A))
A = sorted(A)
print(A)
F.close()
