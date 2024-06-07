#list vs tuple

#list & tuple : order is preserved

l=[1,4,2]
t=(1,4,2)
print("list:",l)
print("tuple:", t)
print("list type:", type(l))
print("tuple type:", type(t))

#duplicates are allowed for both
a=[1,7,3,4,1,5,4]
b=(1,7,3,4,1,5,4)
print("listdup:",a)
print("tupledup:",b)

#list is mutable & tuple is immutable

x=[1,2,3,4,5]
y=(1,2,3,4,5)
x[0]=6
#y[0]=6                #tuple is immutable,hence error
print("lismut:",x)
#print("tuplemut:", y)   #error since tuple is immuatble

#list is growble in nature whereas tuple is not

m=[1,2,3,4,5]
n=(1,2,3,4,5)
m.append(6)
m.remove(4)
n.append(6)            #error since tuple is non-growable in nature
print("listgrow:", m)
