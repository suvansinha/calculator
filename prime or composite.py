num = int(input("Enter a number: "))

if num>1:
    for i in range(2,num):
        if num % i == 0:
            print(num, "is a composite number")
            break
    else:
        print(num, "is a prime number")
elif num==0 or num==1:
    print(num, "is neither prime nor composite number.")

        