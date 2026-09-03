# # Wap a table of 4 .

for i in range (4 , 41 , 4):
    print(i)


for i in range(0 , 101 , 4): # (starting , ending , difference)
    print(i)


# we can use the for loops in all the things in string , in loops and in tuples also

# string
s = "ujjwal"

for i in range(1 , 5 , 2): 
    print(s[i])

# lists
l = ["ujjwal",1 ,23,45,32,4]

for items in l:
    print(items)

for items in range(0,5,2):
    print(l[items])

else:
    print("all items are done")