# Simple calculator

def addition(x, y):
    sum = float(x) + float(y)
    print(sum)


def subtraction(x, y):
    operation = float(x) - float(y)
    print(operation)


def multiplication(x, y):
    multiply = float(x) * float(y)
    print(multiply)


def division(x, y):
    divide = float(x) / float(y)
    print(divide)


def exponentiation(x, y):
    exp = float(x) ** float(y)
    print(exp)


def modulo(x, y):
    modul = float(x) % float(y)
    print(modul)


def get_numbers():
    x, y = (input("Enter two numbers separated by a space: ").split())

    while x.isalpha():
        print("Incorrect format, enter a number")
        x = input("Enter the first number: ")

    while y.isalpha():
        print("Incorrect format, enter a number")
        y = input("Enter the second number: ")

    return x, y


def calculator():
    x, y = get_numbers()
    print(f"x= {x}")
    print(f"y= {y}")

    while True:
        arithmetic = input("What math operation do you want to perform?: ").lower()

        if arithmetic == 'add':
            addition(x, y)

        elif arithmetic == 'subtract':
            subtraction(x, y)

        elif arithmetic == 'multiply':
            multiplication(x, y)

        elif arithmetic == 'divide':
            division(x, y)

        elif arithmetic == 'exp':
            exponentiation(x, y)

        elif arithmetic == 'modulo':
            modulo(x, y)

        elif arithmetic == 'quit':
            quit()

        else:
            print("Enter the correct math operation: (add/subtract/multiply/divide/exp/modulo/quit)")


calculator()
