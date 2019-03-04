from datetime import date
import re
import matplotlib.pyplot as plt

fname = input('Enter the file name: ')

try:
    fhand = open(fname) 
except:
    print('File cannot be opened:', fname)
    exit()

host=[]
lin = 0
count = 0
wrong = 0

d = {1:0,2:0,3:0,4:0,5:0,6:0,7:0} 
d.get('unknown key',0)

for line in fhand:
    lin = lin + 1
    line = line.rstrip()
    if re.search('^Date: (\d{4}-\d{1,2}-\d{1,2})', line):
        count = count + 1
        numbers = re.findall('^Date: (\d{4}-\d{1,2}-\d{1,2})', line)
        ssplit = numbers[0].split('-')
        ssplit = [ int(x) for x in ssplit ]
        dates = date(year=ssplit[0],month=ssplit[1],day=ssplit[2])
        host.append(dates.isoweekday())
        
if lin == 0:
    print('The file is empty!')
elif count == 0:
    print('Can not find the data in the file!')
else:
    for c in host:
        d[c]= d.get(c,0)+1

    name_list = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']  
    num_list = [d[7],d[1],d[2],d[3],d[4],d[5],d[6]]
    plt.bar(range(len(num_list)), num_list,color='kygcbmr',tick_label=name_list)  
    plt.show()