# Dictionary 
a = {} # empty dict
ujjwal = {
    "marks" : "100",
    "iq" : "180",
    "packs" : "6 packs",
    "net_worth" : ["1.5 Trillion Dollar" , "Perth Villa" , "London Mansion"],
    "speech" : ("I would like to take this chance to say Thanks to me " , "Thanks for me on beleiving on me",
    "When there is no one i am broken there is only two thing with me , me and my shiva my god " ,
    "I Know without shiva power and energy i cant become which i am today Thanks to all of you")
}

print(ujjwal.keys())
print(ujjwal.items())
print(len(ujjwal))
print(type(ujjwal))


(ujjwal.update({"marks" : 102}))
print(ujjwal)

ujjwal["marks"] = 103
print(ujjwal)