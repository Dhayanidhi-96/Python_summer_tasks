'''
Task 1: Write a calculator that supports +, -, *, / with user input and exception handling.
'''
while True:
    try :
        a = float(input("Enter your first number :"))
        b = float(input("Enter your second  number :"))
        op = input("Select your operator (+,-,*,/):")
        if op == "+":
            result = a+b
        elif op == "-":
            result =  a-b
        elif op == "*":
            result =  a*b
        elif op == '/':
            try : 
                result = a/b
            except ZeroDivisionError:
                print("Error : You cannot divide by zero")
                result =  None
        else :
            print("Invalid operator!:")
            result = None

        if result is not None:
            print("Result",result)
    except ValueError:
        print("NOt a valid number!")

    again = input("Doyou wan to continue calculation (yes/No):").lower()
    if again == "no" or again == "exit":
        print("Thankyou ! Good bye !")
        break

