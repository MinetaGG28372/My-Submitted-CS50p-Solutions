def main():
    speech = input("Insert some speech with smiley face or sad face: ")
    convert(speech)

def convert(text):
    y1 = text.replace(":)","🙂")  #replace smiley faces, and the result replaces the original speech
    y2 = y1.replace(":(","🙁") #replace the result above with sad faces, and have our result replaced
    print(y2)

main()
