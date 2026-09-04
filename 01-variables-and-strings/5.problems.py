# # display user entered name followed by good afternoon
# a = input("Enter your name : ")
# b = 19
# print(f"Good Afternoon{a}" , "\n" f"happy birthday to you {a}" , f"now you r {b} years old") 
# use f string it is new feature use to gives the values of variables mtlb , lagane ki kio jarurat nhi na + (concat karne ki).

# # input name and date 
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''

date = (input("Enter the date :"))
Name = input("Enter the name :")

print(f"Dear {Name} ", "\n" f"You are selected ! {date}") # more concise
print(f"Dear {Name} You are selected ! {date}") # both are good