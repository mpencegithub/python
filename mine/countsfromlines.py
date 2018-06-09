fhandle=open('mbox-short.txt')
words=list()
count=0
for line in fhandle :
    line = line.rstrip()
    if line.startswith('From:') : continue
    if line.startswith('From') :
        words=line.split()
        address=words[1]
        print(address)
        count=count+1
print('There were',count,'lines in the file with From as the first word')
