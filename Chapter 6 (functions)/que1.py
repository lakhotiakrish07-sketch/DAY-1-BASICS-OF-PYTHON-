# . Write a program using functions to find greatest of three numbers. 
def greatest(a,b,c):
    if(a>=b and a>=c):
        print(f"{a} is greater then {b} and {c} ")
    elif(b>=a and b>=c):
        print(f"{b} is greater than {a} and {c} ")   
    else:
        print(f"{c} is greater than {b} and {a}")\


greatest(9.5,6.5,7)