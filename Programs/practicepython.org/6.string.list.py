# Ask the user for a string and print out whether this string is a palindrome 
# or not. 
string = str(input('Give a string to check for palindrome\n')).strip()
print(f'"{string}" is ', end='')
palindrome = True if string == string[::-1] else False
print('Palindrome' if palindrome else 'Not a palindrome')