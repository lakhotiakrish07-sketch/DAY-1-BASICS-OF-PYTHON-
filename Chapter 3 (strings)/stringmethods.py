a = "harry ????????????"
#strings are immutable means they cannot be changed
#let we want to make latter capital
print(a.upper()) #HARRY ????????????
print(a.lower()) #harry ????????????
print(a.capitalize()) #first letter capital
print(a.title()) #first letter of each word capital 
print(a[2].upper()) #R
print(a.replace("harry", "krish")) #krish ????????????
print(a.replace("?", "i")) #harry iiiiiiiiii
print(a.count("r")) #2
print(a.rstrip("?")) #removes ? from right side
print(a.find("rr")) #2 (gives starting index of substring)
print(a.find("xyz")) #-1 (if substring not found)
print(a.index("rr")) #2 (gives starting index of substring)
print(a.index("xyz")) #throws error if substring not found
print(a.startswith("har")) #True
print(a.endswith("???")) #True
print(a.split(" ")) #splits string at space and makes list ['harry', '????????????']
print(a.split("?")) #splits string at ? and makes list ['harry ', '',

# '', '', '', '', '', '', '', '', '', '']
print(a.strip("?")) #removes ? from both sides
print(a.replace("?", "").strip()) #removes ? from both sides and extra spaces
print(a.center(50, "*")) #centers string in 50 width with * as fill character
print(a.ljust(50, "-")) #left justifies string in 50 width with - as fill character
