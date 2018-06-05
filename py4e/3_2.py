# This first line is provided for you

score = input("Enter Score: ")
try:
    fscore = float(score)
except:
    print("Error: Please type a Numeric Number")
    quit()
try:
    fscore > 0.0
    fscore <=1.0
except:
    print("Error: Please enter a number between 0.0 and 1.0")


if fscore >= 0.9 :
    fscore = 'A'
elif fscore >= 0.8 :
    fscore = 'B'
elif fscore >= 0.7 :
    fscore = 'C'
elif fscore >= 0.6 :
    fscore = 'D'
elif fscore < 0.6 :
    fscore = 'F'
print(fscore)
