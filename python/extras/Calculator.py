# By Tom Pell

while True:
    choice = input("Type Add\Sub\Mult\Div: ")
    if choice == "Add":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1 + num2)
    elif choice == "Sub":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1 - num2)
    elif choice == "Mult":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1 * num2)
    elif choice == "Div":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1 / num2)
    else:
        print("Error Wrong Input")
