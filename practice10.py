def qiyin_parol(pasword):
    return len(pasword) >= 8

pasword = input("Parolni kiring : ")

if qiyin_parol(pasword):
    print("Tushadi : ")
else:
    print("Xavfsizlik uchun kamida 8 ta bolishi kerak")