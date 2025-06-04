def main():
    t = input("What time is it? ")
    if 7.0 <= convert(t) <= 8.0:
        print("breakfast time")
    elif 12.0 <= convert(t) <= 13.0:
        print("lunch time")
    elif 18.0 <= convert(t) <= 19.0:
        print("dinner time")

def convert(time):
    h, m = time.split(":") # split into hours and minutes by a colon
    h = int(h) # convert into numerical datatype
    m = int(m) / 60
    return h + m # representation in hours

if __name__ == "__main__":
    main()

# Big idea: timestamps can be seen as a real number in hours. We consider the input and timerange representations accordingly
# By the ##:## format, the part before and after the colon are hours and minute. The split operator using : does the work, and we convert the input to hours

