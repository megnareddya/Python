print("*****Numeric datatypes:int,float,complex,bool**********")
a=2
b=3
c=6.8
d=True
e=False
f=8+9j
g=1111
h=0b1111
i=123
j=0o123
k=456
l=0x456
m=0xBeef
n=1.9e7


print(g)             #decimal system
print(type(g))
print(h)             #since 0b is mentioned, it is binary number(0,1 are allowed).Now,equivalent decimal number is printed
print(type(h))
print(i)             #decimal system
print(j)             #since 0o is mentioned,it is octal(0-7 are allowed).Now,equivalent decimal is printed
print(k)             #decimal system
print(l)             #since 0x is mentioned, it is hexadecimal(0-9,A-f are allowed).Now equivalent decimal is printed
print(m)             #since 0x is mentioned, it is hexadecimal.Now equivalent deciaml is printed
print(type(a))         #datatype of a
print(id(a))           #address of a
print(a)               #value of a
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(float(a))
print(int(c))
print(complex(a,b))
print(type(True))
print(a>b)
print(int(True))
print(float(True))
print("c:",c)            #float value, general decimal system
print("n:",n)            #float value,exponential form

print("***************")

print("******Sequence data types*********")

x=[1,2,3]
print(x)
print(type(x))

y={1,2,3,1,2}
print(y)
print(type(y))

z=(1,2,3)
print(z)
print(type(z))

w="megna"
print(w)
print(type(w))


print(range(5))
print(type(range(5)))



print("***************")

print("Hello", "World", 123, True, 3.14)
print("Hi, My name is Megna", "Reddy",sep=" - ")

print("2*****")

print("Hi", "Megna", "Reddy",sep="-",end="\t")
print("Hi", "Megna", "Reddy")

print("3*****")

print("Hi","Megna","Reddy",sep="+",end="*")
print("Line2")

print("4*****")

print("I am Good Person", end="_")
print("I am Bad Person")

print("5*****")

print(max(10, 23))
print(max(10, 23, 45))
print(max(10, 23, 45, -1, -2, 100, 1, 87.34))
#print(max(10, 23, 45, -1, -2, 100, 1, "Megna"))   #this is error

print("6*****")

# print("Hello World")        #this is also error because of tab at the starting of line

print("7*****")

# Dynamic Type - Type of Data that Python supports.
age = 65
# variableName = variableValue
# identifier = literal

# Types which are supported in the Python

# Integers - Positive and negative whole numbers.
# 1, -1,123, 999, 100000, 96543210

# Floating Points Numbers
# 3.14, 5.3333333 , 18.00, 0.000786  . -0.4, -1.6
pi = 3.14

# String
# "pramod", "A", "hello world", "Hi, I am good person, You are a liar", "12345"
name = "Pramod"

# Boolean
# True, False
# true, false ? boolean?
isMale = True

# How do I check the type of the variable?
print(type(age))
print(type(name))
print(type(isMale))
print(type(pi))

# Python - Complex NUMBER - i iota -
complex_number = 2 + 3j
# Real - 2
# Imaginary - 3
print(complex_number.real)
print(complex_number.imag)

# Complex Data types in Python
# List
# Tuple
# Dictionary
# Set

print("8*****")

age = 65
# Dynamically typed
print(type(age))
agee= "sixty five"
print(type(agee))

print("9*****")

name=34
print(type(name))
print(name)

print("10*****")

namee="megna"
print(type(namee))
print(namee)


print("11*****")

a=23
b=-23
c=2.3
d=-2.3
e="megna"
f='reddy'
g= "sony"
h= 'sonyy'
i=True
j=False
k= True
l= False
#m=true                          #gives error since it shpuld be defined as True but not true
#n=false                         #gives error since it shpuld be defined as False but not False

print("a:")
print(type(a))
print(a)

print("b:")
print(type(b))
print(b)

print("c:")
print(type(c))
print(c)

print("d:")
print(type(d))
print(d)

print("e:")
print(type(e))
print(e)

print("f:")
print(type(f))
print(f)

print("g:")
print(type(g))
print(g)

print("h:")
print(type(h))
print(h)

print("i:")
print(type(i))
print(i)

print("j:")
print(type(j))
print(j)

print("k:")
print(type(k))
print(k)

print("l:")
print(type(l))
print(l)

print("m:")
print(type(m))
print(m)                     #gives error

print("n:")
print(type(n))
print(n)                    #gives error








