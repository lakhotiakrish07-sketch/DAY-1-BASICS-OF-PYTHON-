    #       *
    #      **
    #     ***
    #    ****
    #   *****
#it consist of two triangle one is dectriangle of spaces and another is inc triangle of *
n=5
for i in range(n):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i+1):   
        print("*",end="") 
    print()    