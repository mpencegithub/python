fhandle=open('mbox-short.txt', 'r')
counts=dict()
largest = None
address=None
#Gets all address's and counts them
for line in fhandle :
    if line.startswith('From:') : continue
    if line.startswith('From') :
        #print(line)
        words=line.split()
        #print(words[1])
        address=words[1]
        #print(address)
        counts[address]=counts.get(address,0) + 1
        #print(counts.items())


for key,value in counts.items():
    num=value
    name=key
    # print(num)
    # print(name)
    if largest is None :
        largest = num
        address = name
    elif num > largest :
        largest = num
        address = name
    # print(largest)
    # print(address)
string=str(largest)
print(address + ' ' + string)
