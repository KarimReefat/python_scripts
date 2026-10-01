import os

r = os.listdir('/home/karim/Desktop/Cache/gif')
w = 0
for i in r:
    w += 1
    z = str(w)
    os.system('mv /home/karim/Desktop/Cache/gif/{0} /home/karim/Desktop/Cache/gif/{1}'.format(i, z + '.gif'))

print('yes')

r = os.listdir('/home/karim/Desktop/Cache/gif1')
w = 0
for i in r:
    w += 1
    z = str(w)
    os.system('mv /home/karim/Desktop/Cache/gif1/{0} /home/karim/Desktop/Cache/gif1/{1}'.format(i, z + '.gif'))

print('yes')

r = os.listdir('/home/karim/Desktop/Cache/jpeg')
w = 0
for i in r:
    w += 1
    z = str(w)
    os.system('mv /home/karim/Desktop/Cache/jpeg/{0} /home/karim/Desktop/Cache/jpeg/{1}'.format(i, z + '.jpeg'))

print('yes')

r = os.listdir('/home/karim/Desktop/Cache/jpeg1')
w = 0
for i in r:
    w += 1
    z = str(w)
    os.system('mv /home/karim/Desktop/Cache/jpeg1/{0} /home/karim/Desktop/Cache/jpeg1/{1}'.format(i, z + '.jpeg'))

print('yes')


r = os.listdir('/home/karim/Desktop/Cache/png')
w = 0
for i in r:
    w += 1
    z = str(w)
    os.system('mv /home/karim/Desktop/Cache/png/{0} /home/karim/Desktop/Cache/png/{1}'.format(i, z + '.png'))

print('yes')

r = os.listdir('/home/karim/Desktop/Cache/png1')
w = 0
for i in r:
    w += 1
    z = str(w)
    os.system('mv /home/karim/Desktop/Cache/png1/{0} /home/karim/Desktop/Cache/png1/{1}'.format(i, z + '.png'))

print('yes')
