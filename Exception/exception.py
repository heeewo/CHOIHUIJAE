# SyntaxError, 잘못된 문법이나 표현을 사용해 주었을 때 발생한다
# IndentationError, 파이썬에서 굉장히 중여한 들여쓰기가 잘못되었을 때 발생합니다
# ZeroDivisionError, 0으로 다른 숫자를 나누려 했을때 발생하는 에러
# 등등 더 여러 에러가 존재 이런 오류를 예외처리하는 방법
# 1. try ~ except : 메세지 변수에 뭐가 오류인지 조금 친절하게 설명해줌
# try :
#	실행할 코드
# except 에러이름 as 메세지변수 :
#	에러 발생시 실행할 코드
# 2. try ~ else : except와 같지만 아닐시 실행할 else를 붙여줌
# try :
#	10 / 2
# except 에러이름 as 메세지변수 :
#	에러 발생시 실행할 코드
# else:
#	예외의경우 실행할 코드
# 3. try ~ finally : 실행할 코드가 에러가 떠도 finall밑의 코드를 실행시킴
# try :
# 	실행할 코드
# finally 
