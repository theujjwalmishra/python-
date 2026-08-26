# in the list we can add many types of data types 
list_1 = ["Ujjwal","Mishra",56,False]
list_2 = [23,32,45,65,13]
a = list_1[0:3]
print(a)

b = list_1[0]
c = list_1[2]
print(b)
print(c)
print (f"{b}"f"{c}")

list_2.sort()
print(list_2)
list_2.reverse()
print(list_2)
list_2.append(8)
print(list_2)
list_2.insert(3,8) # add 8 at index 3
print(list_2)
a = "i am ujjwal"
x = a.find("am")
print(x)