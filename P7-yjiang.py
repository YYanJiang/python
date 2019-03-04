fname = input('Enter the file name: ')

try:
    fhand = open(fname) 
except:
    print('File cannot be opened:', fname)
    exit()

host=[]
lin = 0
count = 0

for line in fhand:
    lin = lin + 1
    line = line.rstrip()
    
    if line.startswith('From:'):     
        print(line)
        
        ##count = count + 1
        '''words = line.split()
        
        if not words[1] in host: 
            host.append(words[1])


if lin == 0:
    print('The file is empty!')    
elif count == 0:
    print('Can not find the data in the file!') 
else :
    print('The file has',len(host),'sender email addresses.')'''