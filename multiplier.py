# this program print multiples of a number less than 100
  
n = int(input("enter your no. ="))

if n> 100 or n<0:
     print("not possible")
if n == 0:
     print("0")     

    
for i in range(1,101):
   if 1<=i*n<= 100:
     print(i*n)
    
    
    
   
    
       

    
