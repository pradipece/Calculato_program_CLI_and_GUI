# Advance level Calculator Program
print("Welcome to calculator program")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Input the quit (q)")

# Function for the option
def addition(num1,num2):
    add = num1+num2
    return add

def subtraction(num1,num2):
    sub = num1-num2
    return sub

def multiplication(num1,num2):
    mul = num1*num2
    return mul

def division(num1,num2):
    div = num1-num2
    return div

#use while loop
while True:
    option = input("Select an option for calculation option(+ , - , * , / ):  ")
    match option:
        case "+":
            num1 = int(input("Enter the 1st number: "))
            num2 = int(input("Enter the 2nd number: "))  
            print("Addition is: ", addition(num1,num2)) 
        
        case "-":
            num1 = int(input("Enter the 1st number: "))
            num2 = int(input("Enter the 2nd number: "))  
            print("Subtraction is: ", subtraction(num1,num2)) 
        
        case "*":
            num1 = int(input("Enter the 1st number: "))
            num2 = int(input("Enter the 2nd number: "))  
            print("Multiplication is: ", multiplication(num1,num2)) 
        
        case "/":
            num1 = int(input("Enter the 1st number: "))
            num2 = int(input("Enter the 2nd number: "))  
            print("Addition is: ", division(num1,num2)) 
        case q:
            print("Input the q for quit: ")
            break
            
           