# hour = int("enter hours in 24 hour format: ")

# if hour<12:
#     print("good morning")
# elif hour>12 and hour<18:
#     print("good afternoon ")
# else:
#     print("good evening")

#using time module
import time 
timestamp = time.strftime("%H:%M:%S")
print("current time is :", timestamp)
if timestamp < "12:00:00" :
    print("good morning")
elif timestamp >= "12:00:00" and timestamp < "18:00:00":
    print("good afternoon")
else :   
    print("good evening")