# Task: counting input/ count numbers and letters

# Write a program that accepts letters and numbers and returns the quantity of numbers and letters inputted.
# Extend the program to count and return the quantity of upper and lower case characters inputted.


user_input = input('Enter words and/or numbers: ')
counted = {"Numbers": 0, "Letters": 0, "Upper": 0, "Lower": 0}

for item in user_input:
    if item.isalpha():
        counted["Letters"] += 1

        if item.isupper():
            counted["Upper"] += 1

        elif item.islower():
            counted["Lower"] += 1

    elif item.isdigit():
        counted["Numbers"] += 1

print(counted)

# or

numbers = []
letters = []
upper = []
lower = []

user_input = input('Enter words and/or numbers: ')

for item in user_input:
    if item.isalpha():
        letters.append(item)

        if item.isupper():
            upper.append(item)

        elif item.islower():
            lower.append(item)

    elif item.isdigit():
        numbers.append(item)

print(f'Letters: {len(letters)}')
print(f'Numbers: {len(numbers)}')
print(f'Upper: {len(upper)}')
print(f'Lower: {len(lower)}')
