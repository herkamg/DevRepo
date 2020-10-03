# exercise 5_2

largest = None
smallest = None
while True:
    num = input("Enter a  Natural number: ")
    if num == "done" :
        break
    try:
        fval = int(num)
    except :
        print('Invalid input')
        continue
    #print(num)
    if largest is None:
        largest = fval
        smallest = fval
        continue
    if fval > largest:
        largest = fval
    if fval < smallest:
        smallest = fval
print("Maximum is", largest)
print("Minimum is", smallest)
