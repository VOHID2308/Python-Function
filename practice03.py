def is_even(number):
    return number % 2 == 0 

def print_even_massage(number):
    print(f"{number} juft son ")

def print_odd_massage(number):
    print(f"{number} Toq son ")


def main():
    son = int(input("Sonni kiritng : "))
    if is_even(son):
        print_even_massage(son)
    else:
        print_odd_massage(son)


main()