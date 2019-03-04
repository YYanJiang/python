fname = input('Enter the file name: ')

try:
    fhand = open(fname) 
except:
    print('File cannot be opened:', fname)
    exit()

host=list()
count = 0
wrong = 0

import re

for line in fhand:
    line = line.rstrip()
    if re.search('^New Revision: [0-9.]+', line):
        numbers = re.findall('^New Revision: ([0-9.]+)', line)  
        try:
            numbers = [ int(x) for x in numbers ]
            host=host+numbers
            count = count + 1
        except:
            wrong = wrong + 1

if wrong != 0:
    print('Have',wrong,'bad datas!')
if count == 0:
    print('Can not find the data in the file!')
else:
    #if have bad datas, calculate the residue datas
    ave=round(sum(host)/count,1)
    print('Average =',ave)
    print('Number of lines=',count)