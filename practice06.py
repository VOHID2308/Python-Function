def is_valid_phone_number(phone):
    return len(phone) == 9

phone = input("Number : ")
if is_valid_phone_number(phone):
    print("Togri")
else :
    print("Xato ")