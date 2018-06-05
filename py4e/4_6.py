hours = input('Number of Hours Worked:')
rate = input('Rate of Pay:')
try:
    hours=float(hours)
except:
    print('Enter Hours as an integer')
    quit()
try:
    rate=float(rate)
except:
    print('Enter Rate as an integer')
    quit()
if hours > 40:
    othours = (hours - 40)
else:
     othours = 0

def computepay():
    pay = (hours * rate) + (othours * (.5 * rate))
    return pay
print(computepay())
