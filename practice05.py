from random import randint

def check_guess(secret , guess):
    return secret == guess

def print_result(is_correct):
    if is_correct:
        print("Togri topdingiz ")
    else :
        print("topa olmadiz ")

def main():
    secret = randint(1, 9)

    guess = int(input("taxminiy son kiriting : "))

    is_correct = check_guess(secret, guess)
    print_result(is_correct)


main()