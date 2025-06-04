# Basic approach:
'''def main():
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

main()'''

# DANGER: if we are to swap the positions of '.pdf' and '.txt' (this one to come first in dictionary), then our file is recognized as a txt file, thus a false result
# Core idea: filetype depends on the extension, which lies exactly at the end of filename
# The stringmethod "endswith" seems reasonable enough to fit this requirement

#Refined version:
def main():
    print(filetype("File name: ")) #Two functions composed as one

def filetype(p):
    file = input(p).lower().strip(" ")
    M = {'.gif': 'image/gif',
        '.jpg' : 'image/jpeg ',
        '.jpeg' : 'image/jpeg ',
         '.png' : 'image/png',
         '.pdf':'application/pdf',
        '.txt' : 'text/plain',
        '.zip' : 'application/zip'
        }                                      #basic dictionary format: {key1: value1, key2: value2, ..., key_n: value_n}

    for i in M:
        if file.endswith(i):
            return M[i]         # We can also use: return M.values(i)
        else:
            continue            #the else part can be skipped, it eventually performs the next iteration

    return 'application/octet-stream'

main()
    
