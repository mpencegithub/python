import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET


while True:
    webaddress = input('Enter webaddress: ')
    if len(webaddress) < 1: break


    uh = urllib.request.urlopen(webaddress)
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    print(data.decode())
    tree = ET.fromstring(data)
### New code
    comments = tree.findall('.//comment')
    print('Type comments', type(comments))
    numbers=list()
    print('Type Numbers', type(numbers))
    for item in comments:
        print('Count', item.find('count').text)
        number=item.find('count').text
        number=int(number)
        numbers.append(number)
    print('Sum', sum(numbers))
