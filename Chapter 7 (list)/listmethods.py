l = [ 1,2,3,4,5]
print(l)
#methods
l.append(7)
print(l)
l.sort(reverse=True)
print(l)
print(l.index(1))
print(l)#[7,5,4,3,2,1]
m=l.copy()
#make m as a copy of list l
m.insert(1,98)
print(m)
print(l.count(1))

#m is a copy so process in m do not change l
n = [900,1000,1100]
l.extend(n)
print(l)
#it means open n and put in the list of n
# we also do that 
k = l + n
print(k)