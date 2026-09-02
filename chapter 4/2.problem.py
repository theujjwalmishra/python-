subject_1 = int(input("Enter the Numbers : "))
subject_2 = int(input("Enter the Numbers : "))
subject_3 = int(input("Enter the Numbers : "))

Total_Marks = (subject_1 + subject_2 + subject_3)/3

if(subject_1 >= 33 and subject_2 >= 33 and subject_3 >= 33 and Total_Marks >= 40):
    print("You are Pass")

else:
    print("You are Fail")