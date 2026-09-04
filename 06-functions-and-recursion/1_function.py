def greet():
    # print("Good Day") # print will give none also
    return "Good Day"

a = input("Enter the Name ")
print(f"{greet()} MY {a}")