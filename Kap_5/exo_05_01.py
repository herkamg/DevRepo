# exercise 5_1
Average = 0.0
count = 0
tot = 0.0
snumber = None
number = 0

while True:
    snumber = input("please, enter a numeric: ")
    if snumber == 'done':
        break
    try:
        number = float(snumber)
    except :
        print('Invalid input')
        continue
    count = count + 1
    tot = tot + number
Average = tot / count
print('Total:', tot, 'count:', count, 'Average:', Average)
