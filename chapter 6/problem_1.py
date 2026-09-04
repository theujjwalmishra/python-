# Wap using fucntion to find the greatest of three numbers

def greatest(a , b , c):
    if(a > b and a > c):
        return a
    elif(b > a and b > c ):
        return b
    else:
        return c

x= greatest(1,2,3)
print(x)