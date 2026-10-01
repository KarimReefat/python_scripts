import cProfile

def fab(n):
	a = 0
	for b in range(n+1):
		a += b
	print(a)
	return a

def fab1(n):
	a = (n/2) * (n+1)
	print(a)
	return a

def fabs(n):
	a = fab(n[0]-1)
	b = fab(n[-1])
	return print(b - a)

def fabs1(n):
	a = fab1(n[0]-1)
	b = fab1(n[-1])
	return print(b - a)

def ran(n):
    a = 0
    l = []
    while True:
        a += 1
        l.append(a)
        if a == n:
            break
    return l

def ran1(n):
    l = []
    for a in range(n):
        l.append(a)
    return l

def ran2(n):
        l = list(range(n))
        return l



##cProfile.run('ran(99**3)')
##cProfile.run('ran1(99**3)')
##cProfile.run('ran2(99**3)')

##l = [10,11,12,13,14,15]
##fabs1(l)
##l = ran(30)
##fabs1(l)



