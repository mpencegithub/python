# This first line is provided for you

hrs = input("Enter Hours:")
flhrs = float(hrs)
if flhrs > 40.0 :
    flot = flhrs-40.0
else :
    flot = 0.0
rte = input("Enter Rate of Pay:")
flrte = float (rte)
#print(type(flhrs))
#print(type(flot))
#print(type(flrte))
pay = ((40 * flrte) + (flot * (1.5 * flrte)))
print(pay)
