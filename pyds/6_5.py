#Find the number at the end and convert to floating point
text = "X-DSPAM-Confidence:    0.8475"
stnum=text.find(' ')
lstnum=len(text)
num=text[stnum+1:lstnum]
flnum=float(num)
#intnum=num
print(flnum)