def main():
    m = int(input("Enter the mass: "))
    print(f"The corresponding energy is E = {einstein(m)}J")

def einstein(KL):
    c = 3 * pow(10,8)
    return KL * pow(c,2)

main()
#16 zeroes! There's gotta be a way to clean this up
