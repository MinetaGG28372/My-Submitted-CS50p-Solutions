string_s = input("Insert a name in camelCase: ")
for c in string_s:
    if c.isupper(): #replace this uppercase character with "_[its lowercase version]"
        c = f"_{c.lower()}"
        print(c, end="") #Ensuring the characters are printed without creating a new line
    else:
        print(c, end="") #Since by default, print("some_text_here") is by default the same as print("some_text_here", end="\n")
