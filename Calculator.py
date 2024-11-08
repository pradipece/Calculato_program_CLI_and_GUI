
print("Welcome to basic calculator program")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")


num1= int(input("Enter the 1st number: "))
option = input("Select an option for calculation option(+ , - , * , / ):  ")
num2= int(input("Enter the 2nd number: "))

if option == "+":
    add= num1+num2
    print("Addition is: " +str(add))
        
elif option == "-":
    sub= num1-num2
    print("Subtraction is: " +str(sub))
    
elif option == "*":
    mul = num1*num2
    print("Multiplication is: " +str(mul))

elif option == "/":
    div = num1/num2
    print("Division is: " +str(div))
else:
    print("Invalid input")



'''
Or

print("Welcome to basic calculator program")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# For the calculator using the basic if and else condition loop

option = int(input("Select an option for calculation option: "))
if option in range (1,5):
        num1= int(input("Enter the 1st number: "))
        num2= int(input("Enter the 2nd number: "))

        if option == 1:
            add= num1+num2
            print("Addition is: " +str(add))
        
        elif option == 2:
            sub= num1-num2
            print("Subtraction is: " +str(sub))
    
        elif option == 3:
            mul = num1*num2
            print("Multiplication is: " +str(mul))

        elif option == 4:
            div = num1/num2
            print("Division is: " +str(div))
else:
    print("Invalid input")

'''


'''
or

# Basic calculator python program 
    print("Welcome to basic calculator program")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    option = int(input("Select an option for calculation option: "))
    if option in range (1,5):
        num1= int(input("Enter the 1st number: "))
        num2= int(input("Enter the 2nd number: "))

        if option == 1:
            add = num1+num2
            print("Addition is: ", num1,"+", num2, "=", add)
        
        elif option == 2:
            sub = num1-num2
            print("Subtraction is: ", num1,"–", num2, "=", sub)
        
        elif option == 3:
            mul = num1*num2
            print("Multiplication is: ", num1,"*", num2, "=", mul)

        elif option == 4:
            div = num1/num2
            print("Division  is: ", num1,"/", num2, "=", div)
    else:
        print("Invalid input")
'''