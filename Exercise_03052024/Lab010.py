#frozenset
#order is not preserved

a={1,2,3,4,5}
b=frozenset(a)
print(b)
print(type(b))
print(a)
print(type(a))

#duplicates are not allowed
x={1,2,3,4,5,1,2,3,4,5}
y=frozenset(x)
print(y)

#indexing,slicing is not allowed since order is not preserved
z={1,2,3,4,5}
w=frozenset(z)
#print(w[0])

#immutable
p={1,2,3,4,5}
q=frozenset(p)
q.add(6)
