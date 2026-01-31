def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def devide(n1, n2):
    return n1 / n2

def calculator(operator):
    if operator == "*":
        return multiply
    elif operator == "+":
        return add
    elif operator == "-":
        return substract
    elif operator == '/':
        return devide
    else:
        print("Periksa inputan anda")
        return None

should_accumulate = True
n1 = float(input("What's the first number?: " ))

while should_accumulate:
    print("\n +\n -\n *\n /\n")
    operator = input("Pick an operation: ")
    n2 = float(input("What's the next number? "))

    operation = calculator(operator)

    # mengecek apakah operator valid dan melanjutkan jika valid
    if operation:
        result = operation(n1, n2)
        print(f"{n1} {operator} {n2} = {result}")
    else:
        print("Operasi tidak valid")

    choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start new calculation")

    if choice == 'y':
        n1 = result
    else:
        should_accumulate = False
        print("\n" * 20)





