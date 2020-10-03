# this file should find the smallest number in a list of number
#smallest_so_far = +1e+48
smallest_so_far = None
numbers = [9, 41, 12, 3, 74, 15 ]
print('before', smallest_so_far)
for number  in numbers:
    if smallest_so_far is None:
        smallest_so_far = number
    if number < smallest_so_far:
        smallest_so_far = number
        break;
    print(smallest_so_far, number)
print('after', smallest_so_far)
6
