# wap to write the table

# Function to print table
def print_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# Taking input from the user
num = int(input("Enter a number: "))

# Calling the function
print_table(num)
