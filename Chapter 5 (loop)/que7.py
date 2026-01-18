# Write a program to print the following star pattern. 
#   *    i=0
#  ***      i=1
# ***** for n =  3          i=2 


#it consist if three triangle dec tringle of space + inc odd no of * triangle + inc triangle of space 
n=3
for i in range(n+1):
    for j in range (n - i):
        print(" ",end="")
    for j in range(2*i - 1):
        print("*",end="")
    for j in range (n - i):
        print(" ",end="")  
    print()
            
        
