# Here's the solution I came up with (not good enough)
def main():
    text = input("Input: ")
    delete_vowels(text)

def delete_vowels(s):
    vowels = ["a","e","i","o","u"]
    print("Output: ",end="")

    last = s[-1]
    first = s.replace(last,"")

    for c in first:
        if c.lower() in vowels:
            c = ""
            print(c, end="")
        else:
            print(c, end="")

    if last.lower() in vowels:
        print("")
    else:
        print(last)

main()

#Here's the refined version, assisted by the programming community and AI (just for education purposes)
'''def main():
    text = input("Input: ")
    print("Output:", end=" ")
    print(remove_vowels(text))

def remove_vowels(s):
    vowels = "aeiouAEIOU"
    return ''.join(c for c in s if c not in vowels)

main()'''
