# decreasing triangle 
# *****
# ****
# ***
# **
# *

n = int(input("num:"))
for i in range(n):
    for j in range (n-i):
        print("*",end="")
    print()    
