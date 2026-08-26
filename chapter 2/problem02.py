# WAP a program to accept the marks of 6 students and display them in sorted manner.
Students =[]
Student1_marks = int(input("Enter the marks : "))
Student2_marks = int(input("Enter the marks : "))
Student3_marks = int(input("Enter the marks : "))
Student4_marks = int(input("Enter the marks : "))
Student5_marks = int(input("Enter the marks : "))
Student6_marks = int(input("Enter the marks : "))

Students.append(Student1_marks)
Students.append(Student2_marks)
Students.append(Student3_marks)
Students.append(Student4_marks)
Students.append(Student5_marks)
Students.append(Student6_marks)

Students.sort()
print(Students)

