import re
'''
Regex operation for identifying user defined words
'''
file=open("user.txt",'r')
for line in file:
    word = str(line).split()
    if re.search('[A-Z]*[a-z]+[0-9]+[a-z]*', str(word)) is not None:
        print(re.search('[A-Z]*[a-z]+[0-9]+[a-z]*', str(word)))
