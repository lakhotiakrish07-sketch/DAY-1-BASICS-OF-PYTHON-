# Write a program to find out whether a given post is talking about “Harry” or not. 
topic = input("enter the topic")

a = topic.count("harry")
if a != 0 :
    print("they are talking about harry")
else:
    print("you are not the topic")