fname = input('Enter the file name: ')

try:
    fhand = open(fname) 
except:
    print('File cannot be opened:', fname)
    exit()

host=[]
lin = 0
count = 0

d = dict() 
d.get('unknown key',0)

for line in fhand:
    lin = lin + 1
    line = line.rstrip()
    
    if line.startswith('From:'):
        count = count + 1
        
        words = line.split()  
        key = words[1]
        host.append(words[1])
        
if lin == 0:
    print('The file is empty!')    
elif count == 0:
    print('Can not find the data in the file!') 
else:
    for c in host:
        d[c]= d.get(c,0)+1

    print("\n The email address and the number that sent the most emails is:")
    print(max(zip(d.keys(),d.values())))
