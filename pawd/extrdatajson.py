import urllib.request, urllib.parse, urllib.error
import json


while True:
    numbers=list()
    sub=0
    url= input('Enter Location: ')
    if len(url) < 1: break

    print(url)
    uh=urllib.request.urlopen(url)
    data=uh.read().decode()
    print('Retreived Data', len(data))

    js= json.loads(data)

    print(json.dumps(js, indent=2))
    print('length', len(js["comments"]))
    jscom=js["comments"]
    print(jscom)
    for item in jscom:
        number=js["comments"][sub]["count"]
        print(number)
        number=int(number)
        numbers.append(number)
        print(sub)
        sub=sub+1
        print(sub)
    print('Sum', sum(numbers))
