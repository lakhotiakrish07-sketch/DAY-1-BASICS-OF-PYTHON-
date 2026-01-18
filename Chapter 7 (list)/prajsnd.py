# def sum(a,b):
#     sum = a + b
#     print(sum)

# sum(2,4)    #function call

# def goodday(name):
#     print(f"good day {name}")

# name  = input("whatis your name:")
# goodday(name)    

# def name(name="stranger"):
#     print(name)

# name1 = input("what is your nmae:")
# name(name1)
# name()  

def factorial(n):
    if(n==0 or n==1):
        return 1
    n = n* factorial(n-1)
    return n 

a= 5
print(factorial(a))