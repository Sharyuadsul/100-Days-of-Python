def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


calc = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    n1 = float(input("Enter the First Number: "))
    for operator in calc:
        print(operator)

    continue_calc = True
    while continue_calc:
        operator = input("Enter the Operation: ")
        n2 = float(input("Enter the Next Number: "))

        function = calc[operator]
        answer = function(n1, n2)
        print(f"{n1} {operator} {n2} = {answer}")

        chain = input(f"Enter 'y'to continue with {answer} or type 'n'to start new calculation: ")
        if chain == "y":
            n1 = answer
        elif chain == "n":
            continue_cal = False
            calculator()


calculator()

