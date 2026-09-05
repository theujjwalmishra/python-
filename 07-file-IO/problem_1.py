# wap to read the txt create a file "poem.txt" and find the twinkle in the poem

with open("poem.txt","w") as a:
    a.write("Twinkle Twinkle little star ")

with open("poem.txt") as b:
    c = b.read()

if("Twinkle" in c):
    print("there is twinkle")
else:
    print("NO")