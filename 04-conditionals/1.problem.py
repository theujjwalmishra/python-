# greatest of four numbers

a = int(input("Enter the Number"))
b = int(input("Enter the Number"))
c = int(input("Enter the Number"))
d = int(input("Enter the Number"))

if(a > b and b > c and c > d):
    print("A is the Greatest")

elif(b > a and b > c and c > d):
    print("B is the Greatest")

elif(b > a and b < c and c > d):
    print(" C is the Greatest")

else:
    print(" D is the Greatest")