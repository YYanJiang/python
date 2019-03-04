fname = input('Enter the file name: ')

try:
    fhand = open(fname) 
except:
    print('File cannot be opened:', fname)
    exit()

host=[]
count = 0
wrong = 0
#inp = fhand.read()

for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):

        atpos = line.find('X-DSPAM-Confidence:')
        sppos = line.find(' ',atpos+20) 

        try:
            host.append(float(line[atpos+20:sppos]))
            count = count + 1           
        except:
            wrong = wrong + 1

if wrong != 0:
    print('Have',wrong,'bad datas!')
if count == 0:
    print('Can not find the data in the file!')
else:
    #if have bad datas, calculate the residue datas
    ave=round(sum(host)/count,4)
    print('Average spam confidence:',ave)