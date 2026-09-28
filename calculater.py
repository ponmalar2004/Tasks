calculater = float(input("Enter the Number: "))

while True:
    operation = input("Enter operation  : ")
    if operation == "=":
        print("calculater =",calculater)
        break
    if operation not in ["+", "-", "*", "/","%","**"]:
        print("Invalid operation")
        continue
    
    Number = float(input("Enter the Number: "))

    if operation == "+":
        calculater = calculater + Number
    elif operation == "-":
        calculater = calculater - Number
    elif operation == "*":
        calculater = calculater * Number
    elif operation == "/" :
        calculater = calculater / Number
    elif operation == "%":
        calculater = calculater % Number
    elif operation == "**":
        calculater = calculater ** Number