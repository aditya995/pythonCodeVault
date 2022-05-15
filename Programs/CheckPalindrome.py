# Palindrome check
n1 = '454'  # string to be ckecked
bool = (n1 == n1[::-1])  # reversed and checked if they are same
print(bool)  # True if palindrome

# Palindrome check using if-else
str1 = '4224'
str2 = str1[::-1]
if (str1 == str2):
    print('yes palindrome')
else:
    print('No, not a palindrome')
