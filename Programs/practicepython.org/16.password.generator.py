# Write a password generator in Python. Be creative with how you generate 
# passwords - strong passwords have a mix of lowercase letters, uppercase 
# letters, numbers, and symbols. The passwords should be random, generating a 
# new password every time the user asks for a new password. Include your 
# run-time code in a main method.

# Extra:
# 1.Ask the user how strong they want their password to be. For weak passwords,
# pick a word or two from a list.
import string
import random as rn
capital_letters = string.ascii_uppercase
lower_letters = string.ascii_lowercase
special_letters = string.punctuation
numbers = string.digits
for i in range(50):
    # print('Input password strength level: (1-4)\n(1)very weak -> only lowercase alphabets')
    # print('(2) weak -> both lowercase and uppercase')
    # print('(3) Strong -> alphabet with numbers')
    # print('(4) Very Strong -> alphabets, numbers, special characters')
    strength = 4 #int(input())
    # print('To get a strong password length needs to be atleast 8.')
    input_choice = 8 #int(input("Enter the length of your password: "))
    if strength == 1:
        password = [lower_letters[rn.randint(0,len(lower_letters))] for i in range(0, input_choice)]
    elif strength == 2:
        lengthOfLowercase = rn.randint(1,input_choice-1)
        password = [lower_letters[rn.randint(0,len(lower_letters)-1)] for i in range(0, lengthOfLowercase)]
        lengthOfUppercase = input_choice-lengthOfLowercase
        password += [capital_letters[rn.randint(0,len(capital_letters)-1)] for i in range(0, lengthOfUppercase)]
        rn.shuffle(password)
        print('*** lo', lengthOfLowercase, 'Up', lengthOfUppercase)
    elif strength == 3:
        lengthOfLowercase = rn.randint(1,input_choice-2)
        password = [lower_letters[rn.randint(0,len(lower_letters)-1)] for i in range(0, lengthOfLowercase)]
        lengthOfUppercase = rn.randint(1,input_choice-lengthOfLowercase-1)
        password += [capital_letters[rn.randint(0,len(capital_letters)-1)] for i in range(0, lengthOfUppercase)]
        lengthOfNumber = input_choice-lengthOfUppercase-lengthOfLowercase
        password += [numbers[rn.randint(0,len(numbers)-1)] for i in range(0, lengthOfNumber)]
        rn.shuffle(password)
        print('*** lo', lengthOfLowercase, 'Up', lengthOfUppercase, 'Nu', lengthOfNumber)
    elif strength == 4:
        lengthOfLowercase = rn.randint(1,input_choice-3)
        password = [lower_letters[rn.randint(0,len(lower_letters)-1)] for i in range(0, lengthOfLowercase)]
        lengthOfUppercase = rn.randint(1,input_choice-lengthOfLowercase-2)
        password += [capital_letters[rn.randint(0,len(capital_letters)-1)] for i in range(0, lengthOfUppercase)]
        lengthOfNumber = rn.randint(1,input_choice-lengthOfLowercase-lengthOfUppercase-1)
        password += [numbers[rn.randint(0,len(numbers)-1)] for i in range(0, lengthOfNumber)]
        lengthOfSpecial = input_choice - lengthOfLowercase - lengthOfUppercase - lengthOfNumber
        password += [special_letters[rn.randint(0,len(special_letters)-1)] for i in range(0, lengthOfSpecial)]
        rn.shuffle(password)
        print('*** lo', lengthOfLowercase, 'Up', lengthOfUppercase, 'Nu', lengthOfNumber, 'Sp', lengthOfSpecial)
    password = ''.join(password[0:input_choice])
    print(str(password))