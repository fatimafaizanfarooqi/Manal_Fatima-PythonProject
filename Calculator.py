
def calculator():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter only numbers")
        return
    operation = input("enter the operation you want (+ - / *) ")
    if operation == '+':
        print(num1," + ",num2," = ",(num1+num2))
    elif operation =='-':
        print(num1,"-",num2,"=",(num1-num2))
    elif operation =='*':
        print(num1,"*",num2,"=",(num1*num2))
    elif operation =='/':
        if num2 == 0:
            print("Error: Division by zero")
        else:
            print(num1,"/",num2,"=",(num1/num2))
    else:
        print("Invalid operation")
calculator()