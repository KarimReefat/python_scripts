import math

def nth_square_root(a):
    # you simble give this function a radical of a number and it will give the factors of this radical number :
    # lets say that the radical of number 50 is the square root of 25 multiply in the number 2
    b = factors(a)
    for c in range(0,len(b),2):
        d = (b[c],b[c+1])
        e = (is_perfect_square(d[0]),is_perfect_square(d[1]))
        if True in e:
            print d
    
def is_perfect_square(a):
    # this fanction will tell you if a number is a perfect square or not the perfect square number is the number that it's root is a int number
    # not a fraction like 25 and 36 and 9 and 81
    b = str(math.sqrt(a))
    c = b.find('.')
    if len(b[c+1:]) > 1:
        return False
    else:
        return True

def factors(a):
    # this function will give you the factors of a number so the factors of 6 is [2,3] and the factors of 24 is [2, 12, 3, 8, 4, 6]
    l = []
    for b in range(2,a):
        if a % b == 0 and b not in l and a/b not in l:
            l.append(b)
            l.append(a/b)
    return l

nth_square_root(172)
##print 'yes'
##nth_square_root(150)
##print 'yes'
##nth_square_root(72)


    
    
