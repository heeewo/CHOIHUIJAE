# 더러운 학업주의자들을 위한 프로그램 만들기
Student_score = []
Sum = 0
Studend_highscore = []
for i in range(10):
    Student_score.append(int(input("학생의 성적을 입력하시오 :")))
    Sum += Student_score[i]
    if Student_score[i] >= 90:
        Studend_highscore.append(Student_score[i])

print(Sum/len(Student_score))
print(len(Studend_highscore))
######################################################################
# 피타고라스 정리에 만족하는 삼각형 구하기
triangle90 = []
for a in range(1, 51):
    for b in range(1, 51):
        for c in range(1, 51):
            if a**2 + b**2 == c**2:
                triangle90.append([a, b, c])

print(tuple(triangle90))
######################################################################
# 서로 다른 주제의 특강을 둘다 들은 학생들의 명단과 인원수를 계산하여 출력하는 프로그램
import random
first_class = set()
second_class = set()
name_tableA = ["김철수", "박철수", "최철수", "이철수", "김맹구", "박맹구", "최맹구", "이맹구"]
name_tableB = ["김훈", "박훈", "최훈", "이훈", "김유리", "박유리", "최유리", "이유리"]
name_tableC = ["김짱구", "박짱구", "최짱구", "이짱구", "김영희", "박영희", "최영희", "이영희"]
name_tableD = ["김철희", "박철희", "최철희", "이철희", "김영수", "박영수", "최영수", "이영수"]
name_table = name_tableA + name_tableB + name_tableC + name_tableD
while(1):
    if len(first_class) == 10:
        break
    else:
        first_class.add(name_table[random.randint(0, 31)])
while(1):
    if len(second_class) == 15:
        break
    else:
        second_class.add(name_table[random.randint(0, 31)])

both = first_class & second_class
print(both, len(both))
#####################################################################
# 영희가 화석이라서 메모리(RAM)을 걱정하면서 사진을 찍어야 됨으로 사진의 해상도를 구하는 프로그램
def Picxel(s):
    A = list(map(int, s.split('*')))
    return A[0]*A[1]*A[2]


picxel = input("가로*세로*심도 순으로 입력하시오 :")
result = int(Picxel(picxel))
print(result, "bit\n", result/2**3, "byte\n", result/2**13, "kbyte")
print(result/2**23, "Mbyte")

