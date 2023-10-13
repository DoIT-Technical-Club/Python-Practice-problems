num = int(input("Enter a number: "))

if num == 1:
    print(num, "is a composite number.")
elif num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is a Composite number.")
           print(i,"times divided",num//i,"is",num,".")
           break
   else:
       print(num,"is a prime number.")
    
else:
   print(num,"is a composite number.")

if num%2==0:
    print(num,"is a Even Number.")
else:
    print(num,"is an Odd Number.")