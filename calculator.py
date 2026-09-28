print("it's calculator for your clarification")

first_value = int(input("Enter Number : "))
operator = input("Enter Operator : ")
second_value = int(input("Enter Number : "))

if operator == '+': 
    print("Sum of Your Two Numbers", first_value + second_value, "\nYou clarify your doubt\nThanks for Using our Calculator")

elif operator == '-': 
    print("Difference of Your Two Number", first_value - second_value, "\nYou clarify your doubt\nThanks for Using our Calculator")

elif operator == '*': 
    print("Multiple of Your Two Numbers", first_value * second_value, "\nYou clarify your doubt\n\nThanks for Using our Calculator")

elif operator == '**': 
    print("Exponent of Your Two Numbers", first_value ** second_value, "\nYou clarify your doubt\nThanks for Using our Calculator")

elif operator == '/': 
    if second_value == 0: 
        print("Error: Cannot divide by zero") 
    else: 
         print("Division of Your Two Numbers", first_value / second_value, "\nYou clarify your doubt\nThanks for Using our Calculator")

elif (operator == exit):
    print("Exiting the calculator")


else: 
    print("Invalid Operator")
