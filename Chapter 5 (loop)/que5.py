# 5. Write a program to find the sum of first n natural numbers using while loop
n = int(input("write the number :"))
sum  = 0 
i= 0
while(i<=n):
    sum = sum + i 
    i = i + 1 

print(sum)
print(f"sum using formula = ",((n*(n+1))/2))