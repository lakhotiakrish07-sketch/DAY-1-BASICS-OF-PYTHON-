#  Write a program to calculate the grade of a student from his marks from the 
# following scheme: 
# 90 – 100 => Ex 
# 80 – 90 => A 
# 70 – 80 => B 
# 60 – 70  =>C 
# 50 – 60 => D 
# <50        
# => F

marks = int(input("enter your marks out of 100"))
if marks >=50 and marks <60 :
    print("d")
elif marks >=60 and marks <70:
    print("c" )
elif marks >=70 and marks <80:
    print("b")
elif marks>=80 and marks <90:
    print("a")
elif marks <=100 and marks  >90:
    print("ex")
else:
    print("fail")
