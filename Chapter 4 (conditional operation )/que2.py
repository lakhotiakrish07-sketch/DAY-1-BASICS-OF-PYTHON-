#  Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user.
#total marks of each subject is 75
#3SUBJECTS MARKES INPUT > 33 PERCENT IN EACH SUBJETS VARIAVLE > 40 PERCENT IN COMPLTE VARIAVLE > IF ELSE USE AND SHOW PASS AND FAIL 
s1 = int(input("marks of subject 1 out of 75  "))
s2 = int(input("marks of subject 2 "))
s3 = int(input("marks of subject 3 "))

require1 = (s1/75)*100
require2 = (s2/75)*100
require3 = (s3/75)*100

requiredtotal = ((s1 + s2 + s3)/225)*100

if (require1 > 33 and require2 >33 and require3 > 33 and requiredtotal >40 ):
    print("you are passed ")
else :
    print("you are failed ")
