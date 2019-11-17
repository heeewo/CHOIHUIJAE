name = input() ; age = int(input()) ; height = float(input())

print("제 이름은 {0}입니다.\n제 나이는 {1:0>10d}입니다.\n제 키는 {2: <8.2f}cm입니다." .format(name,age,height))
