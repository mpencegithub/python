fname=input('Please Enter a File Name: ')
#fname='mbox-short.txt'
count=0
total=0
try:
    fhandle=open(fname)
except:
    print('File does not exist ', fname)

#Process the lines and Count them
for line in fhandle :
    if not line.startswith('X-DSPAM-Confidence: '):
        continue
# Remove Newlines aka Whitespace
    nline=line.rstrip()
    #print(nline)
    count=count+1
    #print(count)
    spnum=line.find(' ')
    lstnum=len(line)
    #print('Start: ', spnum+1)
    #print('End: ', lstnum)
    num=line[spnum+1:lstnum]
    flnum=float(num)
    #print(flnum)
    total=total+flnum
    #print(total)
print('Average spam confidence: ', total/count)
#print(count)
