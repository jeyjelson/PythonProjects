from art import logo
print(logo)
def add(n1, n2):
    return n1 + n2

def subtract(n1 ,n2):
    return n1 - n2

def multiply(n1 ,n2):
    return n1 * n2

def divide(n1 ,n2):
    return n1 / n2

math_dictionary = {"+": add, "-": subtract, "*": multiply, "/": divide}

continue_calculations = True
while continue_calculations == True:
    first_num = int(input("input first number"))

    for operators in math_dictionary:
        print(operators)
    continue_with_number = True

    while continue_with_number == True:
        total = 0
        operation = input("choose an operator")
        second_num = int(input("input second number"))
        calculation = math_dictionary[operation](first_num,second_num)

        print(calculation)
        continue_calc = input(f" y to continue with {calculation} n for new calculation")
        if continue_calc == "n":
            calculation = 0
            continue_with_number = False
            print("\n" * 20)
        elif continue_calc == "y":
            continue_with_number = True
            first_num = calculation


# If no, program asks the user for the fist number again and wipes all memory of previous calculations.
# Add the logo from art.py