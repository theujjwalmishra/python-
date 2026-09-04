# Scam Detection

Message = input("Enter the message : ")

p1 = "Make a lot of money"
p2 = "Buy Now"
p3 = "subscibe this"
p4 = "click this"



if(p1 in Message or p2 in Message or p3 in Message or p4 in Message):
    print("Scam")

else:
    print("Safe")