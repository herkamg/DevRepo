#  program to prompt for a score between 0.0 and 1.0
score = input("Enter Score: ")
try:
    fscore = float(score)
except :
    fscore = float(score)
    print("Error, please enter numeric input")
    quit()

if fscore<0.0 or fscore>1.0:
    print ("Error, score out range, Score schould be between 0.0 und 1.0")
    quit()

if fscore >= 0.9:
    print("A")
elif fscore >= 0.8:
    print("B")
elif fscore >= 0.7:
    print("C")
elif fscore >= 0.6:
    print("D")
elif fscore < 0.6:
    print("F")
