#  Q1) Accept a string and count vowels, consonants,digits,spaces & special character
string = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
spaces = 0
special = 0

vowel_set = set("aeiouAEIOU")

for char in string:
    if char.isalpha():  
        if char in vowel_set:
            vowels += 1
        else:
            consonants += 1
    elif char.isdigit():  
        digits += 1
    elif char.isspace():  
        spaces += 1
    else:  
        special += 1

print("Vowels: ", vowels)
print("Consonants: ", consonants)
print("Digits: ", digits)
print("Spaces: ", spaces)
print("Special Characters: ", special)
