# lecture on regular expression.
# regular expression is a form of a language,
# it's a way to say that a set of strings
# match or don't match a regular expression.

# re.Search() return true or false

import re

##search or find expression
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
# #    if line.find('From:')>=0:
#     if re.search('From:', line):
#         print(line)
# # startswith expression
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
# #    if line.startswith('From:'):
#     if re.search('^From:', line):
#         print(line)
# print("this excercise is funny")

# # regex "*"= 0 or more times
# # regex "."= the dot character matches any character
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('^X.*:', line):
#         print(line)
# print("this excercise is funny")

# regex "\S"= non blank character
# regex "+"= 1 or more times
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X\S+:', line):
        print(line)
print("this excercise is funny")
