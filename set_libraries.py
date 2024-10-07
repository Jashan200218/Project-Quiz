# Defining a Set
# name=set({"Alice","Elina",'Sejal',"Naina","Sammi","Alice"})
# print(name)

# methods

# frozenset()
# def froze(x):
#     print(x)
    
# x=froze(frozenset(['abc','123','abc','sdf','456']))    

# Set add()
# def addition(adds):
#     adds.add(6)
#     print(adds)
    
# addition({"jan",'feb','mar','apr','may'})   

# Set clear()
# def clean(months):
#     months.clear()
#     print(months)
    
# clean({'jan','feb','mar','apr','may','june','july','aug','sept','oct'})     

# Set copy()
# six_months=set({'jan','feb','mar','apr','may','june'})
# def copied(six_months):
#     cpoies=six_months.copy()
#     print(six_months)
#     print(cpoies)
    
# copied(set({'jan','feb','mar','apr','may','june'}))    

# Set difference()
# def diferent(prime,num):
#     print(prime.difference(num))
    
# diferent(set({2,3,5,7,11,13,17}),set({1,2,3,4,5,6,7,8,9,11})) 

# Set difference_update()
# def update(a,b):
#     print(a)
#     a.difference_update(b)
#     print("a : ",a)
    
# update(set({'a','c','d','w','e'}),set({'b','d','e','f','w'}))       

# Set discard()
# def discar(num):
#     print(num)
#     num.discard(3)
#     print(num)
    
# discar(set({1,2,3,4,5}))    

# Set intersection()
# def intersect(month,months):
#     print(month)
#     after=month.intersection(months)
#     print(after)
    
# intersect(set({'jan','feb','mar','apr','may','jun',}) , set({'mar','apr','may','july','sept','oct'}))    

# Set intersection_update()
# def updates(a,b):
#     print(a)
#     ans=a.intersection_update(b)
#     print(ans)
    
# updates(set({1,2,3,4}) , set({2,3,4}))    

# Set isdisjoint()
# def joint(x,y):
#     print(x)
#     z=x.isdisjoint(y)
#     print(z)
    
# joint(set({1,2,3,4,5,6,6}),set({7,8,9,10,11,11,}))   

# Set issubset()
# def subset(c,d):
#     a=c.issubset(d)
#     print(a)
    
# subset(set({2,4,6,8,10}),set({1,3,5,7,9}))     

# Set issuperset()
# def super(x,y):
#     z=x.issuperset(y)
#     print(z)
    
# super(set({"mango",'apple','orange'}),set({'mango','apple','orange'}))    

# Set pop()
# def popset(a):
#     b=a.pop()
#     print(b)
#     print(a)
    
# popset(set({1,2,3,4,5,6,7}))    

# Set remove()
# def removes(x):
#     y=x.remove(2)
#     print(x)

# removes(set({2,3,4,5,6,12,34}))    
    
    
# Set symmetric_difference()
# def symmter(x,y):
#     z=x.symmetric_difference(y)
#     print(z)
    
# symmter(set({1,12,3,13,4,14}),set({1,12,5,15,6,16})) 

# Set symmetric_difference_update()
# def updatation(a,b):
#     a. symmetric_difference_update(b)
#     print(a)  
    
# updatation({11,13,15,17,19},{11,13,14,16,18,20})    

# Set union()
# def unions(x,y):
#     z=x.union(y)
#     print(z)
    
# unions({1,2,3,4,},{5,6,7,8})    

# Set update()
def updated(v,w):
    z=v.update(w)
    print(v)
    
updated({"mon","tue","wed"},{"thur","fri"})    