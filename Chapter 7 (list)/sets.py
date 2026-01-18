#sets are the unordered collection of data ,immutable , do not contaian repeated values 
a = {1,2,3,4,5,3,2}
print(a)
#quiz
b ={}#it act as dict as dict also include curly braces 
print(type(b))
c = set()
print(type(c))
#how to axcess sets items
name={"krish","aman","naitik","raj"}
for values in name:
    print(values)#we can get in any order 

#add(x)
name.add("ranjan")
print(name)    

#update(iterable)
name.update(["lambu,neil"])
print(name)

#remove(x)
name.remove("ranjan")
print(name)

#discard
name.discard("lambu,nail")
print(name)

print(name.pop())#this is like we make spin the wheel game randon name is given

# print(name.clear

b = name.copy()
print(b)
