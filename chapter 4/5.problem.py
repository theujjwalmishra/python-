# Grade of Student from his marks

marks = int(input("Enter the Marks : "))

if(marks > 90):
    print("Excellent")
elif(marks >= 90 and 81):
    print("A")
elif(marks >= 80 and 71):
    print("B")
elif(marks >= 70 and 61):
    print("C")
elif(marks >= 60 and 51):
    print("D")
else:
    print("F")