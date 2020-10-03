import re
summe = 0
value = 0
hand = open('regex_sum_702219.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    if (x):
        print(x)
        for snumber in x:
            value = value + 1
            inumber = int(snumber)
            summe = summe +inumber
        print(summe)
print(value)
print("this excercise is funny")
