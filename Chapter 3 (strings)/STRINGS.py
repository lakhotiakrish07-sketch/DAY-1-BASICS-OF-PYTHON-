name = "krish"
age = "24"
brother = 'vishesh'
print("my name is " + name + "my age is " + age + "my brother name is " + brother)
#triple single quotes(use for multiple line string)
address = ''' my name is krish 
lakhotia an i am 19 year old'''

#accessing characters of string(stsrt from 0 index )
print(name[0]) #k
print(name[1]) #r
print(name[2]) #i
print(name[3]) #s
print(name[4]) #h
# print(name[5]) shows aeero

#using for loop to access each character of string
for character in name:
    print(character)

#string slicing
print(name[0:3])#kri
print(name[1:4])#ris

print(address[0:23])# my name is krish

#we can find length of string using len() function
print(len(name))#5


