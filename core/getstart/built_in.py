"""
    For recording about the language provide
"""

for i,v in enumerate(range(10,15)):
    print(f"i = {i}, v={v}")

##something about list
a = [1,2,3,4,5]
id(a[1])
b=a[1:-1]
id(b(0))
b[0] is a[1] # True, but when assign new value to a b then change locally to each list