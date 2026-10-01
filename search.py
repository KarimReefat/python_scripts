l = [1,2,3,4,5,3,6,7,3,8,9,3]
s = [9,6,3,11,89,9,2,4,1,5,6,7,10]

def srh(l,s):
    i = 0
    l1 = []
    for a in l[i:len(l)]:
        i += 1
        if a == s:
            l1.append(i-1)
    return l1
    
def count(l,s):
    l1 = [a for a in l if a == s]
    print(len(l1))
    
def search(l,s):
    r = []
    if len(str(s)) == 1:
        r = srh(l,s)
    else:
        for al in s:
            r.append(srh(l,al))
    print(r)
    
search(l,3)
count(s,9)
search(l,s)


''' idea script is to make it take more than nested list in one input argument and make search for every one of the elemnts
and give me the result back in other kind of nested list. '''
