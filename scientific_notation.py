b = 2756.96
c = 0.00000574600
def scientific_notation(a):
    i = 0
    if a > 10:
        while a > 10:
            a = a / 10
            i += 1
    else:
        while a < 10:
            a = a * 10
            i -= 1
        a = a / 10
        
    b = str(a) + "e" + str(i)
    d = [(a*(10**i)),(b)]
    return(d)

print(scientific_notation(b))


    
    
