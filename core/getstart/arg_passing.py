"""
    check the reference of passing argument
"""

def modify(k):
    """Case one"""
    k.append(12)
    print("in modify id: ",id(k))
    print("k = ", k)


def reassign(k):
    """Case two"""
    k=[8,9,10]
    print("in reassign id: ",id(k))
    print("k = ", k)


def replace(k):
    """Case three"""
    k[0]=4
    k[1]=4
    k[2]=4
    k[3]=4
    print("in replace id: ",id(k))
    print("k = ", k)

def reassign(k):
    """Returning case"""
    print("in reassign id: ",id(k))
    print("k = ", k)
    return k

m = [1,2,3]
print("original id: ",id(m))
modify(m)
print("after case 1 id: ",id(m))
print("m = ",m)

reassign(m)
print("after case 2 id: ",id(m))
print("m = ",m)

replace(m)
print("after case 3 id: ",id(m))
print("m = ",m)