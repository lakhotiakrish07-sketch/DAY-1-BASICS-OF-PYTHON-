#menuplating tuples  
# fruits = [ i for i in range(1,7): input(f"fruit name {i}:")] tis is wrong in list you cant put: after range 
fruits = [input(f"write fruit{i}") for i in range(1,7)]
print(fruits)