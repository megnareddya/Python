print("***String data type***")
s1="megna"
s2='megna'
s3='''megna'''
print("types1:",type(s1))
print("types2:",type(s2))
print("types3:",type(s3))
print(s1,s2,s3)



#print("meghana          #this will give error since "" & '' cant be used for multi line string literaLS
        #is
      #learning
     # python")

print("triple:",'''meghana
         is
         learning
         python''')

print("one:","'meghana' is a good girl")
print("two:",'"meghana" is a good girl')
print("three:",'''"meghana" is a 'good' girl''')

#index
s='meghana'
print(s[5])       #positive index i.e., left right & starts from 0
print(s[-4])      #negative indes i.e., right left & starts from -1

#slicing
print(s[1:4])     #positive index


#Convert meghana into Meghana
a='meghana'
b=a[0].upper()+a[1:]
print("b:",b)

#convert meghana into meghanA
x="meghana"
y=x[0:6]+x[6].upper()
print("y:",y)
z=x[0:len(x-1)] + x[6].upper()
print("z:",z)

