# Creating Tuples Through Literals
# def tple(days):
#     print(days)
#     info=('Ruhi',24)
#     print("%s is %s years old . " % info)
# days=("monday",1,"Tuesday",2,"wednesday",3,"Thursday",4,"friday")    
# tple(days) 

# Using the tuple() Constructor
# def info(personal_info):
#     print(personal_info)
    
# personal_info=info(tuple(["Ruhi is",23,"years old ."]))

# Indexing
# def indes(info):
#    print(info[2])
    
# info=indes((["Ruhi is ",24,"years old"],["and is a gamer"],["and she plays reaaly well"]))  


# Slicing
# def slicing(abc): 
#     print(abc[3:])
#     print(abc[:6:2])
    
# abc=slicing(("Apple","Ball",'Cash',"donkey",'eat','finish','get','home'))    

# + Concatenating Tuples 
# def concanate():
#     concate=even+odd
#     print(concate)
    
# even=(2,4,6,8,10)   
# odd=(3,5,7,9,11)
# concanate()   

# * multiple concatenation 
# def multi(numbers):
#     multiple=numbers*3
#     print(multiple)
    
# numbers=multi((2,4,6,8,10,(1,3,5,7,9)))

# Functions

# len ()
# def lenght():
#     print(len(brands))

# brands= ("Adidas","Celin","Calvin Klein","Louis Vuitton",["Puma","Gucci"])   
# lenght() 

# min () and max ()
# def mix(number):
#     print(min(number))
#     print(max(number))
    
# number=mix((122,233,343,457,755,76,786.5,854.4,844.49))  

# cmp()

# sum()
# def sums(add):
#     print(sum(add))

# add=sums((12,34,56,67,32,45,67,222,3445,6677))

# sorted()
# def sort(num):
#     print(sorted(num,reverse=False))
    
# num=sort(("ABC","abc","DEF",'def',"GHI",'ghi'))    
  
# reversed()
# def revers(days):
#     print(tuple(reversed(days[::1])))
    
# days=revers(('monday','tuesday','wednesday','thursady','friday','saturday','sunday'))       

# all()
# def alls(abc):
#     print(all(abc))
    
# abc=alls(('a','b','c','d','false',1,2,3,False))  

# any() 
# def ans(odd):
#     print(any(odd))

# odd=ans((1,3,5,7,9,11,"True",False)) 

# # Example with two lists
# def zipp(names,score):
#     zipped=zip(names,score)
#     print(tuple(zipped)) 
    
# zipp(('Alice', 'Bob', 'James','Suzy','lamda'),(85, 90, 95,67,67,56))

# enumerate()
def num(name):
    for i,name in enumerate(name,start=2):
        print(i,name)
        
name=num(("Angel","NAncy","Sam","saafi",'Robin'))        
