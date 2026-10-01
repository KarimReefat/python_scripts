import cProfile 

def nor_rev(a):
    b = a[::-1]
    return b

def my_rev(a):
    i = len(a)
    b = ''
    while i > 0:
        c = a[i-1]
        b += c
        i -= 1
    return b

def my_rev1(a):
    i = len(a)
    b = ''
    while i > 0:
        b += a[i-1]
        i -= 1
    return b

b = 'hello world this is our world so please let it go '
c = b * 999999
cProfile.run('nor_rev(c)')
cProfile.run('my_rev(c)')
cProfile.run('my_rev1(c)')
