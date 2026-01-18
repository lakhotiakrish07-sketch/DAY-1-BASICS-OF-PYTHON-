#one rule of coding dont name module same as standard library module
#nested is if inside s if statemenyt
num = int(input("what is your number "))
if(num<0):
    print("number is negative")
else:
    if(num == 0 ):
        print(f"{num} is zero")
    else:
        print(f"{num} is positive")