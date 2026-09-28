


print("Welcome to Mathematical Operation")
a = int(input("Enter first number: "))
while True:
    operation = input("Select operation or done: ")
    if(operation == "done"):
        print("Exiting the program.")
        break

    b = int(input("Enter next number: "))

    if operation == "+":
        result = a + b

    elif operation == "-":
        result = a - b

    elif operation == "*":
        result = a * b

    elif operation == "/":
        result = a / b

    elif operation == "%":
        result = a % b

    else:
        print("Invalid input!")
        continue
    
    print("Result:", result)
    a = result