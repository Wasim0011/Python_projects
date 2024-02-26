import os   #library for clear screen function

# defining functions
def add(a, b):
    return a+b
def subtract(a, b):
    return a-b
def multiply(a, b):
    return a*b
def divide(a, b):
    return round(a/b, 2)

operation_dict={'+':add,    #creating dictionary of operations
                '-':subtract,
                '*':multiply,
                '/':divide }
def calculator():   #defining calculator function
    num1=float(input("Enter first number: "))
    continue_flag=True
    while continue_flag:
        for symbol in operation_dict:
            print(symbol)
        operation=input("Pick an operation: ")
        num2=float(input("Enter next number: "))
        calculator_function=operation_dict[operation]
        result=calculator_function(num1, num2)
        print(f"{num1} {operation} {num2} = {result}")
        should_continue=input(f"Enter 'y' to continue calculation with {result}, 'n' to start a new calculation or 'x' to exit: ").lower()   #converting in lower case
        if should_continue=='y':
            num1=result
        elif should_continue=='n':
            os.system('cls')    #clearing screen
            continue_flag=False
            calculator()    #calling recursively
        else:
            continue_flag=False
            print("Bye!")
calculator()    #calling for the first time
