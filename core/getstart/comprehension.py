from math import sqrt

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


prime100 = [x for x in range(101) if is_prime(x)]
print(prime100)

a = {x*x: (1,x,x*x) for x in range(20) if is_prime(x)}
print(a)

iterable = ['spring', 'summer', 'autumn', 'winter']
iterator = iter(iterable)
next(iterator)

def first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("Iterable sis empty")

