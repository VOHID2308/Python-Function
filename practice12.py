def hisobla_bmi(vazn: float, boy: float) -> float:
    return vazn / (boy ** 2)

def aniqla_holat(bmi: float) -> str:
    if bmi < 18.5:
        return "Ozg'in (Underweight)"
    elif 18.5 <= bmi < 25:
        return "Normal holat"
    elif 25 <= bmi < 30:
        return "Ortiqcha vazn (Overweight)"
    else:
        return "Semizlik (Obese)"

vazn = float(input("Iltimos, vazningizni kilogrammda kiriting: "))
boy = float(input("Iltimos, bo'yingizni metrlarda kiriting: "))

bmi = hisobla_bmi(vazn, boy)

holat = aniqla_holat(bmi)

print(f"\nSizning BMI ko'rsatkichingiz: {bmi:.2f}")
print(f"Sog'liq holatingiz: {holat}")
