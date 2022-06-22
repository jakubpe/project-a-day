def add(n1, n2):
    return n1 + n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def subtract(n1, n2):
    return n1 - n2


# def taking_input():
#     x = float(input("\nFirst number: "))
#     operation = input("Input operation: ")
#     y = float(input("Second nuber: "))
#     return x, y, operation
operations = {
    '+': add,
    '*': multiply,
    '/': divide,
    '-': subtract
}


def calculator():
    num1 = float(input("\nFirst number: "))
    print("Pick an operation:")
    for key in operations:
        print(key)
    next_operation = True
    while next_operation:
        operation = input("Pick an operation: ")
        num2 = float(input("Next number: "))
        func = operations[operation]
        result = func(num1, num2)
        print("{} {} {} = {}".format(num1, operation, num2, result))
        num1 = result
        next_calc = input("Type 'y' to continue with {}, 'n' to exit or 'new' to start new calculation".format(result))
        if next_calc == 'n':
            next_operation = False
        elif next_calc == 'new':
            calculator()


calculator()

# print("Possible operations are:\n- to subtract\n+ to add\n* to multiply\n/ to divide")
# result = float
# x, y, operation = taking_input()
# next_operation = True
# while next_operation:
#     if operation == '+':
#         result = add(x, y)
#     elif operation == '-':
#         result = subtract(x, y)
#     elif operation == '*':
#         result = multiply(x, y)
#     elif operation == '/':
#         result = divide(x, y)
#     else:
#         print("Wrong operation input")
#     print(result)
#     break