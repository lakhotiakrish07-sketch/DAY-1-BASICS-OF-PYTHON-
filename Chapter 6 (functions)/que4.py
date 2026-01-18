# Write a recursive function to calculate the sum of first n natural numbers
# def natural(num):
#     num1 = 0 
#     i = 0 
#     while(i<=num):
#         num1 = num1 + i 
#         i = i+1
#     # print(f"{num} is the sum of first n mumbers ")
#     return num1

# print(natural(5))    

def natural(num):
    if(num>0):
        num = num + natural(num-1)
    return num

print(natural(10))    