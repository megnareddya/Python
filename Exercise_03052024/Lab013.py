#byte & bytesarray

a=[1,2,3]
print(type(a))
print(a)

print(type(bytes(a)))
b=list(bytes(a))


#bytes only allow till 0-255
#x=[1,245,255,256]       #error
#y=bytes(x)
#print(type(x))
#print("y:",y)

#order is preserved , indexing & slicing avilable
p=[1,2,3]
q=bytes(p)
print(q[1])
r=list(q[1:2])
print(r)


#immutable


#bytearray
#order is preserved, indexing&slicing available
#mutable

m=[1,2,3,4,5]
n=bytearray(m)
print("1:",type(m))
print("2:",type(n))
print("3:",m)
o=list(n)
print("4:",o)
print("5:",type(o))

print("6:",o[1])
print("7:",o[1:4])

o[1]=10
print("8:", o)


