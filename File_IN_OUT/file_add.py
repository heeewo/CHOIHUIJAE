#파일을 쓰기모드('w')로 열면 기존 내용이 삭제되고 새롭게 쓰여집니다
#그래서 파일을 이어쓸려면 추가모드('a')를 사용해야합니다
#파일을 읽고 쓰기도 마찬가지로 open과 close를 합친 함수 with문이 있음
#with open("파일객채/경로", '형식') as f : 파일 객체이름을 지정하고 블록을 만든다

with open("data/add.txt", 'a') as f :
	f.write(input())

with open("data/add.txt", 'r') as b :
	B = b.read()
	print(B)
