import math

n = float(input("Enter your no.: "))
x = float(input("Enter base of log: "))
if n>0 and x>0 and x!=1: 
    print (math.log(n,x))
else:
    print("undefined")
