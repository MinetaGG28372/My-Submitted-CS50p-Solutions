def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s): #The output space for this function is {True, False}
    not_allowed = [",", " ", "!", "?"]
    if len(s)<2 or len(s)>6 or (not s[0].isalpha()) or (not s[1].isalpha()) : #The tests for condition 1,2
        return False
    for i in range(2, len(s)): #The test for condition 4
        if s[i] in not_allowed:
            return False
#We're now left with the digit conditions. We'll consider 3 typical examples: CS50, CS50X, CS05
#The 3.1 number condition: (1st_digit must be non-zero) assume our string contains some digits. Then there exists the first position corresponding to the first digit to that string
    for i in range(2, len(s)): #BIG loop
         if s[i].isdigit():
            if s[i] == '0':
                return False  # first digit can't be 0
            if not s[i:].isdigit():
                return False  # letters after a number
            break
    return True #if not a number, the loop
main()


