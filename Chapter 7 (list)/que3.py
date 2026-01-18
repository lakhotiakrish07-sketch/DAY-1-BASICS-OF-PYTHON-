# Check that a tuple type cannot be changed in python. 
tup = ("krish", "vishesh","jyoti","ahsish")
# tup.append("saroj") sjows error
print(tup)

#if we wANT TO ADD

changetup = list(tup)
changetup.append("saroj")
tup = tuple(changetup)
print(tup)