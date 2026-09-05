# best way to open and close 

# read operations
with open("ujjwal.txt") as a:
    print(a.read())

# with variables
with open("ujjwal.txt") as a:
    b = a.read()
    print()

# write operations
with open("new.txt","w") as a:
    a.write("Any body can do things")

# other functions 

# append operations
with open("new.txt","a") as d:
    d.write("\nokay bye ")

# update 
with open("ujjwal.txt","r+") as e:
    e.write("Ujjwal is the champ . Yes there are bad times come but it is life \nYou have to fight there. You are champion bro .")

# read

with open("ujjwal.txt") as x:
    z = x.read()
    print(z)
