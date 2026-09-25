result = float(input("Enter a Number: "))
while True:
    operator = input("Enter a Operator: ")
    if(operator == '='):
        print(result)
        break
    if(operator not in ['+','-','*','/','%','**']):
        print("Invalid Operator")
        continue
    a = float(input("Enter a Number: "))
    if(operator == '+'):
        result += a
    elif(operator == '-'):
        result -= a
    elif(operator == '*'):
        result *= a
    elif(operator == '/'):
        if(a == 0):
            print("Number is not divisible by 0")
            break
        else:
            result /= a
    elif(operator == '%'):
        result %= a
    elif(operator == '**'):
        result **= a