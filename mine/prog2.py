#program average
print('Input numbers to get average')
print('Type quit to exit')
print('Type reset to start over')
loop = True
count=0
total=0
while loop is True :
    uinum=input('Enter a number: ')
    try:
        uinum=int(uinum)
        count=count+1
        total=total+uinum
        print(count)
        print(total)
        print('Current Average:', total/count)
        continue
    except:
        if uinum.upper()=='QUIT':
            break
        elif uinum.upper()=='RESET':
            count=0
            total=0
            print('Reset Complete')
            continue
        print('Please use numbers.')
        continue