#list data type : order is preserved  & duplicates are allowed

a=[1,2,4,3,1,'meghana']
print(a)
print(type(a))


#indexing & slicing is applicable
x=[1,2,1,4,7,5,'sony']
print("one:",x[1])
print("two:", x[2:6])

#append() & remove()

z=[]
z.append(1)
z.append(2)
z.append(3)
print("append:",z)
z.remove(2)
print("remove:", z)

#list is mutable

t=[1,2,4,3,6,5]
t[2]=10
print("mutable:", t)


