n = int(input("Enter no. of terms you want in the series: "))
first = 0
second = 1
for i in range(n):
    print(first)
    temp = first
    first = second
    second = temp + second