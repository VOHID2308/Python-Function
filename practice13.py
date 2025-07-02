def palindrom(soz):
    return soz == soz[::-1]

soz = input("sozni kiriting : ")
print(palindrom(soz))
