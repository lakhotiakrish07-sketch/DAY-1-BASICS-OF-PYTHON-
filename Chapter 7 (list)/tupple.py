#in list we use []brackets but in tuple we us ()
#list can be change but tuple cant be change 
tup1 = ("krish",1,2,3,4,5)#we need to put','at the last other wise it act as nornal int , char ,string etc
print(type(tup1))
# tup1[0]=5
# print(tup1)it dhows error because in touple it do not change 
#yes we can add things in tuple 
print(tup1[0])
print(tup1[5])  
if "krish" in tup1:
    print("yes krish is present in tuple ")
else:
    print("no")    

tup2 = tup1[1:3]
print(tup2)   
#mostly same as list methods  