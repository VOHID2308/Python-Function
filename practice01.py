def qushish(a,b):
    result = a + b
    return result

def ayirish(a,b):
    result = a - b
    return result

def kopaytirish(a,b):
    result = a * b
    return result

def bulish(a,b):
    result = a / b
    return result

def main ():
    a = float(input(" A ni kiriting : "))
    b = float(input(" B ni kiriting : "))

    op = input("amal (+ - * /): ")

    if op == '+':
        print(qushish(a,b))
    elif op == '-':
        print(ayirish(a,b))
    elif op == '*':
        print(kopaytirish(a,b))
    elif op == '/':
        print(bulish(a,b))
    else :
        print("Xato ")



main()    