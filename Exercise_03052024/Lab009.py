#1.list
#2.tuple
#3.set

#order is preserved inlist & tuple , but not in set

a=[1,2,3]
b=(1,2,3)
c={1, 2, 3}
print(a, b, c)

#duplicates are allowed in list & tuple, but not in set
x=[1, 2, 3, 3]
y=(1, 2, 3, 3)
z={1, 2, 3, 3}
print(x, y, z)

#indexing & slicing is allowed in list & tuple, but not in set
p=[1, 2, 3]
q=(1, 2, 3)
r={1, 2, 3}
print(p[1])
print(q[1])
# print(r[1])      -> gives error bcz indexing is not allowed since order is not preserved in set

#list,set are growble+mutable  & tuple is non-growable+immutable
x=[1, 2, 3]
y=(1,2,3)
z={1,2,3}

x.append(4)
x.remove(3)
x[0]=5
print(x)

z.add(4)
z.remove(3)
print(z)

#y.append(4)     #gives error bcz tuple is non-growable
#y.remove(3)













