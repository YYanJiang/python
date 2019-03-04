def plural(s):
    if s.endswith(('o','ch', 's', 'sh', 'x')):
        snew = s + 'es'

    elif s.endswith(('ay','ey','iy','oy','uy')):
        snew = s + 's'

    elif s.endswith('y'):
        s=s[:-1]
        snew = s + 'ies'
        
    else: snew = s + 's'
    return snew
    

str = input ("please input a sentence\n")
st = str.split()
lis=[]
for i in range(0, len(st)):
    if (st[i].isalpha()):
        output = plural(st[i])
        lis.append(output)
    else:
        print("The input is invalid!")
        print("Please input a valuable sentence！")
        lis=[]  
s = " ".join(lis) 
print (s)