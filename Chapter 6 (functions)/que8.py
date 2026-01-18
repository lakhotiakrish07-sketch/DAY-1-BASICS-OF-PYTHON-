# Write a python function to print multiplication table of a given number.
def table(n):
    for i in range(1,10+1):
        print(f"{n}*{i}=",i*n)
        i=i+1
table(5)        