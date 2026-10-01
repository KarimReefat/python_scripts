import os, pickle, cProfile
## this one to change the files name and extension into number for alot of folder in the same time:
##r = os.listdir('/home/karim/Desktop/pic')
##l = []
##for a in r:
##    l.append('/home/karim/Desktop/pic/' + a.strip())
##
##for a in l:
##    b = os.listdir(a)
##    w = 0
##    for c in b:
##        c = c.replace(' ','\ ')
##        w += 1
##        z = str(w)
##        os.system('mv {0}/{1} {2}/{3}'.format(a,c,a,z + '.jpeg'))
####
####r = os.listdir('/home/karim/Desktop/pic/images/')
####w = 0
####for a in r:
####    w += 1
####    z = str(w)
####    os.system('mv /home/karim/Desktop/pic/images/{0} /home/karim/Desktop/pic/images/{1}'.format(a,z + '.jpeg'))

## this one to list all the files name and sort it with it's size and save this information into text file:
d = os.listdir('/home/karim/Desktop/pic')
l = []
for a in d:
    l.append(a.strip())
      
for b in l:
    os.system('ls -sS /home/karim/Desktop/pic/{0} 1>/home/karim/Desktop/New/{1}.txt'.format(b,b))

#### this one to add the path of every file with it's name and size into one big list with out sorting in the list
#### like the text file: 
r = os.listdir('/home/karim/Desktop/New')
w = []
for a in r:
    f = open('/home/karim/Desktop/New/{0}'.format(a), 'r')
    while True:
        line = f.readline()
        if len(line) == 0 :
            break
        if line.startswith('total'):
            line = f.readline()
        w.append(line.rstrip('\n') + ' ' + '/home/karim/Desktop/pic/{0}/'.format(a.strip('.txt')))

    f.close()

t = []
for a in w:
    t.append(a.split())

d = t
c = []
def sort_1(s):
    for a in s:
        c.append([int(a[0]),a[1:]])
    c.sort()
    
## this one will sort the data in the list that contain the name and size and path of every file and will sort it by
## using the file size and in my case it take very long time and then store the result of the sorting in object file:   
   
def sort(s):
    for a in range(1,len(s)):
        key = s[a]
        key1 = int(key[0])
        i = a - 1
        key2 = s[i]
        key3 = int(key2[0])       
        while i >= 0 and key3 > key1:
            s[ i + 1 ] = s[i]
            i = i - 1
        s[i + 1] = key
##    myfile = '/home/karim/Desktop/list.data'
##    f = open(myfile, 'wb')
##    pickle.dump(s, f)
##    f.close()

print(t[0],d[0])
cProfile.run('sort_1(d)')
cProfile.run('sort(t)')
print(t[0],d[0],c[0]) 
