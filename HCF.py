def computeHCF(a,b):
    if b==0:
        return a
    else:
        return computeHCF(b,a%b)
    
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("The HCF of",num1,"and",num2,"is",computeHCF(num1,num2))
    