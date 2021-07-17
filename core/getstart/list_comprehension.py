from math import factorial

words = "tuoi hong tho ngay, duoi mai truong, au tho da di qua roi".split()
lens = [len(word) for word in words]
print(lens)

f = [len(str(factorial(x))) for x in range(20)]
print(f)