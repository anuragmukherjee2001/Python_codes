str1 = input("Insert Starting letter: ")
str2 = input("Insert ending letter: ")

if str1 >= str2:
    print("Enter the correct sequence")

while str1 <= str2:
    print(str1, end=" ")
    str1 = chr(ord(str1) + 1)
    