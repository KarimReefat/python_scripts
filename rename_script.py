##def like(a,b):
##    c = [c for c in range(a)]
##    d = [d for d in range(b)]
##    for i in c:
##        e = c[i] * d[i]
##        print(c[i], d[i], e)

import os
## This next one will cose to delete the files in the directory and this will happend after asked it to rename the file name
## with it's same name and after this it will be delete it half by half or this is what i think.

while len(os.listdir('/home/karim/Desktop/Cache')) :
    r = os.listdir('/home/karim/Desktop/Cache')
    print(r)
    w = 0
    for i in r:
        w += 1
        z = str(w)
        os.system('mv /home/karim/Desktop/Cache/{0} /home/karim/Desktop/Cache/{1}'.format(i,z + '.jpeg'))

        
##r = os.listdir('/home/karim/Desktop/Cache')
##w = 0
##for i in r:
##    w += 1
##    z = str(w)
##    os.system('mv /home/karim/Desktop/Cache/{0} /home/karim/Desktop/Cache/{1}'.format(i, z + '.jpeg'))

## this for rename in many folder that exist in one folder :
        
##for b in range(1,11):
##    r = os.listdir('/home/karim/Desktop/jpeg/{0}'.format(b))
##    w = 0
##    for i in r:
##        w += 1
##        z = str(w)
##        os.system('mv /home/karim/Desktop/jpeg/{0}/{1} /home/karim/Desktop/jpeg/{0}/{2}'.format(b,i, z + '.jpeg'))
    
