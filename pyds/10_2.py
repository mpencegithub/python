fhandle=open('mbox-short.txt')
counts=dict()
# get the hours from the lines and count them into a dictionary
for line in fhandle :
    if line.startswith('From:') : continue
    if line.startswith('From') :
        words=line.split()
        #print(words[5])
        time=words[5]
        units=time.split(':')
        # print(units[0])
        hours=units[0]
        counts[hours]=counts.get(hours, 0) + 1

#Sort and print the hours and counts
for k,v in sorted(counts.items()) :
    print(k,v)
