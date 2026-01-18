#  Write a program to accept marks of 6 students and display them in a sorted 
# manner.
marks = [int(input(f"marks of student{i}:")) for i in range(1,7)]
marks.sort()
print(marks)