#dictionary

#order is not preserved
#duplicate keys are not allowed,but duplicate values are allowed
a={1:'first',2:'second',3:'third',1:'fourth'}
print(a)
print(type(a))

#idexing,slicing not allowed

#mutable
a[4]='fifth'
print(a)
a[1]='sixth'
print(a)
