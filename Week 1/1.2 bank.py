text = input("Greeting: ")
standardized_text = text.strip().capitalize()   #Avoid situations of case-sensitive and spacebars at both ends
if "H" not in standardized_text:    # To check whether a substring exists inside something or not, use the (in) operator
    print("$100")
elif "Hello" in standardized_text: #We can directly use else (the case that "H" is in standardized_text), but elif structure ensures all cases are separate
    print("$0")
else:
    print("$20")

