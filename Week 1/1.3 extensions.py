def main():
    name = input("Enter the file name: ")
    name = name.lower()
    print(EXT(name))

def EXT(file):
    if ".gif" in file: #1st type
        return "image/gif"
    elif (".jpg" in file) or (".jpeg" in file): #2nd, 3rd type
        return "image/jpeg"
    elif ".png" in file: #4th type
        return "image/png"
    elif ".pdf" in file:  #5th type
        return "application/pdf"
    elif ".txt" in file: #6th type
        return "text/plain"
    elif ".zip" in file: #7th type
        return "application/zip"
    else:
        return "application/octet-stream"

main()
