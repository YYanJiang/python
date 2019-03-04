fname = input('Enter the file name: ')

try:
    fhand = open(fname,encoding='utf-8') 
except:
    print('File cannot be opened:', fname)
    exit()

host=list()
lin = 0
count = 0

dw = dict() 
dw.get('unknown key',0)
dl = dict() 
dl.get('unknown key',0)

for line in fhand:
    lin = lin + 1
    line = line.rstrip()
    line = line.lower()
 
    from string import punctuation
    punc_translator = str.maketrans({key: None for key in punctuation})
    cleanString = line.translate(punc_translator)  
    
    words = cleanString.split()  
    #把line行按空格分隔开存入list words
    
    for i in words:
        for letter in i:
            if letter =="”" or letter=="“" or letter=="’" or letter=="‘" or letter=="﻿":
                continue
            else:
                dl[letter]= dl.get(letter,0)+1
    
        
    host = host + words
    #读到的所有词放入host数组
    
#print(host)
    
if lin == 0:
    print('The file is empty!')    
else:
    for c in host:
        dw[c]= dw.get(c,0)+1
        #已经存在就+1 不在就加入

        
    lst1 = list()
    for key, val in list(dw.items()):
        lst1.append((val, key))
    lst1.sort(reverse=True)
    
    lst2 = list()
    for key, val in list(dl.items()):
        lst2.append((val, key))
    lst2.sort(reverse=True)
    
    print('\nThe total number of words is:',format(len(host),','),'\n')
    
    print('The number of distinct words is:',format(len(dw),','),'\n')
    
    print('The top 25 most frequent words and counts is:')
    for key, val in lst1[:25]:
        print(val,format(key,','))
        
    print('\nCharacter frequency sorted is')
    for key, val in lst2:
        print(val,format(key,','))
        
    