quit = False
print('Type quit at anytime to quit')

while quit is False:
    string=input('enter a letter: ')
    try:
        int(string)
        print('That is an integer')
        continue
    except:
        if string=='quit':
            break
        print('that is a string')