def ask_question(question, correct_answer):
    javob = input(question + "\n>>> ")
    return check_answer(javob, correct_answer)

def check_answer(user_answer, correct_answer):
    return user_answer.lower() == correct_answer.lower()

print(" Mini Quiz Boshladi!")


ball = 0

if ask_question("1. O'zbekiston poytaxti nima?", "Toshkent"):
    print(" To'g'ri!")
    ball += 1
else:
    print(" No to'g'ri!")

if ask_question("2. 2 + 2 nechiga teng?", "4"):
    print(" To'g'ri!")
    ball += 1
else:
    print(" No to'g'ri!")

if ask_question("Eng mashxur dasturlash tili qaysi", "Python"):
    print("Tog'ri!")
    ball += 1 
else:
    print (" No to'g'ri!")

if ask_question("bir kun necha soatdan iborat : ", "24"):
    print("To'g'ri!")
    ball += 1
else:
    print(" No to'g'ri!")

print(f"\nNatija: 4 tadan / {ball} ball")
