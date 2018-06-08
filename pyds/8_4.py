fhandle=open('romeo.txt', 'r')
words=list()
for lines in fhandle :
    line=lines.rstrip()
    pieces=line.split()
    for piece in pieces :
        if piece not in words :
            words.append(piece)
            words.sort()
print(words)
