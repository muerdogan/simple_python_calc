## very simple python calculator.

print("Simple python calculator")
print("Choose what to do:")
print("1-Add")
print("2-Subtract")
print("3-Multiply")
print("4-Divide")

## Choose transactions between 4 above.

transaction = input("Enter transaction(1/2/3/4):")

if transaction not in ('1', '2', '3', '4'):
    print("Invalid input")
   
## if user's transaction choice is between 1-4 then choose number1 and number2.

else:
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))

    getsum = num1 + num2
    subtract = num1 - num2
    multiply = num1 * num2
    divide = num1 / num2

    if transaction == '1':
        print(getsum)

    elif transaction == '2':
        print(subtract)

    elif transaction == '3':
        print(multiply)

    elif transaction == '4':
        print(divide)
        
