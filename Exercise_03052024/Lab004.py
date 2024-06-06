#Numeric data types : int,float,comples,bool

print("int Datatype")
a=10                #a is in decimal system
print("a:",a)

b=1111              #b is in decimal system
print("b:",b)

c=0b1111            #Ob represents 1111 is binary
print("c:",c)       #Ob represents 1111 is binary,hence equivalent decimal is printed

d=0o1111            #0o represents 1111 in octal
print("d:",d)       #0c represents 1111 in octal,hence equivalent decimal is printed

e=0x1111            #0x represents 1111 in hexadecimal
print("e:",e)       #0x represents 1111 is in hexadecimal,hence equivalent decimal is printed




print("float Datatype")

f=1.2                #decimal system
print("f:",f)

g=1.2e3              #exponential form
print("g:", g)





print("complex Datatype")

h=10+20j                  #decimal system
print("h:", h)
i=10.1+20j                #real part can be int & float
j=10+20.1j                #imaginary part can be int & float
print("i:",i)
print("j:", j)

k=10+20.1j                 #real part can be decimal system
l=0b111+20.1j              #real part can be in binary
m=0o1111+20j               #real part can be in octal
n=0x1111+20j               #real part can be in hexadecimal

print("k:", k)
print("l:", l)
print("m:", m)
print("n:", n)

o=10+20.3j                   #imaginary  part can be only in  decimal system
print("o:", o)
#p=10+0b23.7j                 #imaginary part cant be in octal,decimal,hexadecimal




print("boolen Datatype")

q=0
r=1
print("q:",q)
print("r:",r)
print(type(q))
print(type(r))
s=10
t=20
print("s>t:", s>t)
print("addition:",True+False)