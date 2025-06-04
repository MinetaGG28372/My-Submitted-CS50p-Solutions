'''answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
answer = answer.strip(" ")
match answer:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")'''

#The program works assuming the user doesn't mess up by adding a few extra blanks at either ends of the string. In such cases, it will print "No", not desirable.
#To fix this, we can modify the user input s.t. the spacebars at both ends are stripped away
#To make it case-sensitive, notice that variations of "forty-two" (e.g. FOrtY-tWO) and "forty two" (for example fORTy TwO) can be converted to lowercase, and carrying out the process would do the work/


#My almost complete attempt:
answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
answer = answer.strip(" ").lower()
match answer:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")
