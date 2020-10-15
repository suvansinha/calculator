rows = int(input('Enter the number of rows: '))
choice=int(input("1.diff.numbers in a row/2.same numbers in a row: "))

if choice==1:
  for i in range(1,rows+1): 
      for j in range(1,i+1):
        print(j,end = "")
      print()     
elif choice==2:
    for i in range(1,rows+1): 
      for j in range(1,i+1):
        print(i,end = "")
      print()
else:
    print("invalid input")
      