#program to make a simple calculator using functions of basic operations
#define the functions

def addition(x, y):
    """"this function adds two numbers"""
    return x+y
      
def subtract(x, y):
    """"this function subtracts two numbers"""
    return x-y

def multiply(x, y):
    """"this function multiplies two numbers"""
    return x*y

def divide (x, y):
     """"this function divides two numbers"""
     return x/y
    
# take input from user
print("select operation.")
print("1.addition")
print("2.subtract")
print("3.multiply")
print("4.divide")
option=input("Enter option(1/2/3/4): ")
 
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


if option == '1':
    print(num1, "+", num2,"=", addition(num1,num2))
 
elif option == '2':
    print(num1, "-", num2,"=", subtract(num1,num2))
    
elif option == '3':
    print(num1, "*", num2,"=", multiply(num1,num2))       

elif option == '4':
    print(num1, "/", num2,"=", divide(num1,num2))
    
else:
    print("error! invalid input")     
    
