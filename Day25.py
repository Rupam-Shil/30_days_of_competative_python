'''
Write a python method to check whether a string is a valid password or not.
Password Rules:
Should have at least one number.
Should have at least one uppercase and one lowercase character.
Should have at least one special symbol.
Should be between 6 to 20 Characters long.'''


def passwordCheck(password):
    specialChar = ['@', '#', '$', '%', '&']
    flag = True

    if len(password) < 6:
        flag = False
        print("The password must be at least 6 character long")

    if len(password) > 20:
        flag = False
        print("The length of password cannot be more than 20 characters")

    if not any(p.isdigit() for p in password):
        flag = False
        print("The password must contain at least one number")

    if not any(p.isupper() for p in password):
        flag = False
        print("The password must have at lease one uppercase Character")

    if not any(p.islower() for p in password):
        flag = False
        print("The password must have at least one lowercase character")

    if not any(p in specialChar for p in password):
        flag = False
        print("The password must contain one special character")

    return flag


password = input("Enter Password: ")
if passwordCheck(password):
    print("Valid Password")
else:
    print("Invalid Password")
