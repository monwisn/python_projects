# Running total task

# Write a program that accepts 2 types of inputs I and O and a value to keep track of quantities entered into the input.
# Each input should be inputted so to include a value, format:
# example : I-10 O-10, this would return a qty of 0, (10-10-0)

# Users should be able to continually enter an input until all inputs have been entered.
# After each input the user is shown the quantity update.

qty = 0

while True:
    new_value = input('Input "I-N" or "O-N" where "N" is the number e.g: I-10, if you want to exit type "stop": ')

    if new_value[0] == 'O':
        qty -= int(new_value[2:])

    elif new_value[0] == 'I':
        qty += int(new_value[2:])

    elif new_value == 'stop':
        break

    print(qty)

print(f'Final quantity equals: {qty}')

# or

qty = 0

while True:
    x = input("Input (I-N), Output (O-N): ")
    if not x:
        break

    n_value = x.split("-")

    if n_value[0] == "I":
        qty += int(n_value[1])
        print(f"New Total: {qty}")

    elif n_value[0] == "O":
        qty -= int(n_value[1])
        print(f"New Total: {qty}")

    else:
        pass

print(f"Final Quantity: {qty}")
