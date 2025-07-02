#demak bu bizda ikkita tanlov beradigan dastur 
def Celsius(c):# bu celsini franheitga ozgartiradi 
    return c * 9/5 + 32

def Fahrenheit(f):# bu franheitni celsiga ozgartiradi 
    return (f - 32) * 5/9

print("1. Celsis → Franheit")
print("2. Franheit → Celsis")

tanla = input("Tanlov (1 yoki 2): ")

if tanla == "1":
    c = float(input("Celsius kiriting: "))
    print("Fahrenheit:", Celsius(c))

elif tanla == "2":
    f = float(input("Fahrenheit kiriting: "))
    print("Celsius:", Fahrenheit(f))

else:
    print("Xato tanlov!")
