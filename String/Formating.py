# %s문자열 %c문자 1개 %d정수 %f실수/부동소수 %o8진수 %x16진수 %% %자체
name = "heeewo"
age = 24
height = 172.958102

print("my name is %s." %name)

print("%dyears old." %age)
print("my age is %d." %age)
print("my age is %s." %age)
print("my age is %.2f." %age)

print("height %fcm." %height)
print("height %.2fcm." %height)
print("height %dcm." %height)

print("sexual is '%c'." %"남")

print("apear my age to 16 %x, to 8 %o." %(age, age))

print("%10d %010d" %(10, 10))

print("%8s %8d %8s" %("최희재", 6, "컴퓨터공학"))
print("%-8s %-8d %-8s" %("최희재" , 6, "컴퓨터공학"))
