n = int (input("write down the number :"))
i = 2
while(i<n):
    if(n%i==0):
        print("it is not a prime number")
        break
    i=i+1
else:
    print("it is a prime number")
             