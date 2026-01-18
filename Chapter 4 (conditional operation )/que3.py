# A spam comment is defined as a text containing following keywords: 
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
# to detect these spams.
comment =input("enter any thing")
# comment = "buy me now and buy now  and free money"
spam1 =(comment.count("buy now"))
spam2 =( comment.count("free money"))
spam3 =(comment.count("subscribe"))
spam4 =(comment.count("make a lot of money"))

if (spam1!=0 or spam2!=0 or spam3!=0 or spam4!=0):#at mistake i use ans insteed of or so i am gettinf else because i always type one type of scam and and say to type every type os scam
    print("check mate you scammer ")
else :
    print("safe ")

print(spam1)
print(type(spam1))
print(type(spam2))

