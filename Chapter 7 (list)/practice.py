'''marks = [1,2,3,"marks",True]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
# print(marks[5]) gives 
# index of marks is 4 but length of marks is 5

print(marks[-3])#it will convert into posituive index which is length of marks - 3
print(marks[2])

if 2 in marks:
    print("yes")
else:
    print("no")    #same things apply for string as well 

# listname[start:end:jumpindex]    
print(marks)
print(marks[1:4])
print(marks[1:4:2])#jump 1 value in list
print(marks[:]) #marks[0:len(marks)]'''

lst = [i*i for i in range(5)]
print(lst)
#we can use if and loopsin side the list
lst1=[i*i for i in range(5) if i%2==0]
print(lst1)

