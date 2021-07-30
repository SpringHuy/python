"""
    built a nested loop to loop through all elements in nested tuple
    The point here is no matter how many nested level, the loop is generated
"""

tup = (
    (
        ("mot", "hai", "ba"),
        (1,2,3)
    ),
    (
        (
            ("bon", "nam", "sau"),
            (4,5,6)
        )
    ),
    (
        (
            (
                (
                    (
                        (
                            ("bay", "tam", "chin"),
                            (7,8,9)
                        ),
                    ),
                ),
            ),
        ),
    ),

)


def recursive_loop(val):
    """
        recursive loop to access all the elements of any deep nested tuple
    """
    if type(val) is tuple:
        for i in val:
            recursive_loop(i)
    else:
        print(val)

#rep_list = []
def recursive_list(val):    
    """
        receive a any deep nested tuple and convert it to a corresponding nested list
    """
    empl=[]
    for i in val:
        if type(i) is tuple:
            empl.append(recursive_list(i))
        else:
            empl.append(i)
    return empl

#aloha = recursive_list(tup)
#print("ALOHA: ",aloha)             

#print("TEST THE AUTO LOOP")
#recursive_loop(tup

##Reverse nested tuple
def reverse_loop(val):
    empt = ()
    for i in val[::-1]:        
        if type(i) is tuple:
            empt = empt + (reverse_loop(i),)
            print('in ra empt')
            print(empt)
        else:
            empt = empt + (i,)
            print(empt)
    return empt

revtup = reverse_loop(tup)
print("REV TUP: ", revtup)
    

#unpacking
#lower,upper=minmax([1,12,3,4,5,7])
a="a"
b="b"
a,b=b,a

