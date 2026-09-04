a = "Ujjwal"
print(len(a))
print(a[1:6]) # used to cut the values and hamesa index se ek aage tak ki value deni hoti hai
print(a[1:6:2]) # used to cut the values and kitne letters ke baad dusra letter lana hai


# String function

# endswith() checks if a string ends with given text.
print(a.endswith("al")) 
print(a.find("jw")) # used to give the index of any word
print(a.replace("j",  "")) # used to replace
print(a.count("j")) # used to give total occurences
print(a.capitalize()) # used to capitalize the first words
print(a) # string is immutable it means i have done many function but a is always be Ujjwal stored inside a 

