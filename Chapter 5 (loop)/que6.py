    # Write a program to calculate the factorial of a given number using for loop. 
# factorial is n*n-1*n-2.....
n = int(input("write the number:"))
fact = 1
for i in range(1,n+1):
    fact = fact*i

print(fact)


#using while loop
fact = 1
i = 1
while(i<=n):
    fact = fact*i
    i=i+1

print(fact)    