#question1

t=(1,2,3,4)
print(len(t))

#end

#question2

t=(1,2,3,4,5)
print(min(t))
t1=(1,2,3)
print(max(t1))

#end

#question3

t=(1*2*3*4)
print(t)

#end

#question4

a= set()
input1= input("enter the value")
a.add(input1)
b= set()
input2= input("enter the value")
b.add(input2)
print(a-b)

#end

#question5

a= set()
a= set([1,2,3,4,5,6,7,8])
b= set([4,2,7])
print(a>=b)

#end

#question6

a= set()
a= set([2,3,4,5,6])
b= set([1,2,3,4,7])
print(a&b)

#end

#question7

a= input("enter name")
b= input("enter marks")
d={a:b}
print(d)

#end

#question8

dict= {'niki': 1,'shivi':8,'arti':7,}
sortByValuedict = sorted(dict.items(), key = lambda t: t[1])
print (sortByValuedict)

#end


#question9

l= ["M", "I", "S", "S", "I", "S", "S", "I", "P", "P", "I"]
m= l.count("M")
i= l.count("I")
s= l.count("S")
p= l.count("P")
D= {'m':m, 'i':i,'s':s,'p':p}
print(D)

#end






