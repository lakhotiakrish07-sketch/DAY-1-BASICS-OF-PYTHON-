#find wether a number is  prime or not 
#not dividible buy other number exept 1 and itself below it 
number = int(input("write number :"))
# for num in range(2 , number):
#     if(number%num==0):
#         print(f"{number} is not a prime number")
        
#     else:
#         print(f"{number} is a prime number")
       
       #usinf while loop
num =2
while(number%num==0):
       print("it is not a prime number ")
       num = num+1 and num<number
       break
else:
       print("it is a prime number")   

    