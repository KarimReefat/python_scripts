##def like(a,b):
##    c = [c for c in range(a)]
##    d = [d for d in range(b)]
##    for i in c:
##        e = c[i] * d[i]
##        print(c[i], d[i], e)

import os
## This next one will cose to delete the files in the directory and this will happend after asked it to rename the file name
## with it's same name and after this it will be delete it half by half or this is what i think.

##while len(os.listdir('/home/karim/Desktop/Cache')) :
##    r = os.listdir('/home/karim/Desktop/Cache')
##    print(r)
##    w = 0
##    for i in r:
##        w += 1
##        z = str(w)
##        os.system('mv /home/karim/Desktop/Cache/{0} /home/karim/Desktop/Cache/{1}'.format(i,z + '.jpeg'))

##r = os.listdir('/home/karim/Desktop/jpeg')
##w = 0
##for i in r:
##    w += 1
##    z = str(w)
##    os.system('mv /home/karim/Desktop/jpeg/3/{0} /home/karim/Desktop/jpeg/3/{1}'.format(i, z + '.jpeg'))
    
r = os.listdir('/home/karim/Desktop/1')
l = []
d = []
for a in r:
    try:
        os.listdir('/home/karim/Desktop/1' + os.sep + a)
    except OSError:
        l.append(a)
    if a not in l:
        d.append(a)

s = []
w = []
for c in d:
    try:
        os.listdir('/home/karim/Desktop/1' + os.sep + c)
    except OSError:
        s.append(c)
    if c not in s:
        w.append(c)
        
        



