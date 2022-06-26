import string

def password_creator():
    input_choice = int(input("Enter the length of your password: "))
    capital_letters = string.ascii_uppercase
    lower_letters = string.ascii_lowercase
    special_letters = string.punctuation
    numbers = string.digits
    password_list = []
    password_list.extend(capital_letters)
    password_list.extend(lower_letters)
    password_list.extend(special_letters)
    password_list.extend(numbers)

    generated_password = "".join(password_list[0:input_choice])
    print(generated_password)
    save_congirmation = input('Do you want to save your password?(Yes/No): ')

    if save_congirmation == "yes":
        try:
            with open("./password.txt", 'w') as password:
                password.write(generated_password)
                print('Password saved successfully')
        except Exception as ex:
            print('Something went wrong', ex)