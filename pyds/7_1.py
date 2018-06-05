#prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case.
input('Input filename:   ')
try:
    fhand=open('words.txt')
except:
    print('File does not exist')
    quit()
#fstring=fhand.read()
for line in fhand:
    fstring=line.rstrip()
    print(fstring.upper())