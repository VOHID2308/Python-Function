def balni_olish (score):

    if 90 <= score <= 100:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 60 <= score <= 69:
        return "D"
    elif 0 <= score <= 59:
        return "F"
    else :
        return "ERROR"


ball = int(input("Ball : "))
bal2 = balni_olish(ball)


print(bal2)