num = int(input("Enter a number: "))
factorial = 1
if num<0:
    print("Sorry,factorial is undefined for negative number")
elif num==0:
    print("0! is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print(num,'!',"is",factorial)    
    
    