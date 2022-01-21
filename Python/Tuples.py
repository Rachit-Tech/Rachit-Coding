#The value of tuples can't de changes
a=(1, 2, 3, 4, 5, 6, 1, 9, 7, 1)
b=()#Empty tuple
c=(1,)#Tuple with single element
print (a)
print (a[0])
print (a[0:3])
print (a[-4:])

d=[7, 3, 1, 2, 5, 6]
print(d)
d.sort()
print(d)
d.reverse()
print(d)
d.append(8)
print(d)
d.insert(0, 0)
print(d)
d.pop(1)
print(d)
d.remove(5)
print(d)

print(a.count(1))
print(a.index(7))
