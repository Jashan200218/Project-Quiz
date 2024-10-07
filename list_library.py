# ******************************************** LIST LIBRARIES *****************************************************
# list.append(x)
# def appends(x):
#     for y in ['Pencil','Pen','Eraser','Scale','Marker']:
#         x.append(y)
#         print(x)

# x=['Apple','Banana','Orange','Mango','Pineapple']
# appends(x=['Apple','Banana','Orange','Mango','Pineapple'])  

# list.extend(iterable)
# def extends(brands,more_brands):
#     brands.extend(more_brands)
#     print(brands)
    
## brands=['Gucci','Calvin Klein','Mochi','Louis Vuitton','Dior']    
# extends(['Gucci','Calvin Klein','Mochi','Louis Vuitton','Dior'],['Chanel','Levis']) 

#  list.insert(i, x)
# def fruit(fruits):
#     fruits.insert(4,'Banana')
#     print(fruits)
    
# fruit(['Mango','Orange','Apple','Papaya','Grapes'] )

# list.remove(x)
# def remov(list):
#     list.remove('Cricket')
#     print(list)
    
# remov(['Bat','Ball','Gloves','Golf','Tennis']) 

# list.pop([i])
# def popp(games):
#     games.pop()
#     print(games)
    
# popp(['Tennis','Football','Cricket','Boxing','Judo','Skating'])    

# list.clear()
# def clears(numbers):
#     numbers=[number for number in numbers if number!=4]
#     print(numbers)
#     numbers.clear()
#     print(numbers)
    
# clears([4,3,4,3,4,3])    

# list.index(x[, start[, end]])
# fruit_name=['Date','Tangerines','Grapes','Banana','Apple','Pineapple','Mango']
# def indexes(fruit_name):
#     index=fruit_name.index('Tangerines',0)
#     print(f"The index is : {index}")
    
# indexes(['Date','Tangerines','Grapes','Banana','Apple','Pineapple','Mango'])    

# list.count(x)


# clothes=['Shirts','Skirts','Pants','Skirts','T-shirt','Skirts','Coat','Skirts']
# def cloth(clothes):
#     counts=clothes.count('Skirts')
#     print(counts)
    
# cloth(['Shirts','Skirts','Pants','Skirts','T-shirt','Skirts','Coat','Skirts'])  

# list.sort(*, key=None, reverse=False)
# def sorts(brands):
#     brands.sort(key=None,reverse=True)
#     print(brands)
    
# sorts(['Adidas','H&M','Gucci','Levis','Prada','Mochi','CK'])    

# list.reverse()
# def reverses(x):
#     x.reverse()
#     print(x)
    
# reverses(['abc','def','ghi','jk'])    

# list.copy()
# def cpoied(y):
#     copies=y.copy()
#     print(y)
#     print(copies)
    
# cpoied (['a','b','c','d','e','f','g','h'])   

# Using Lists as Queues
# from collections import deque
# def deques(queue):
#     queue.append('Acounts')
#     print(queue)
#     queue.append('History')
#     print(queue)
#     queue.popleft()
#     print(queue)
#     queue.popleft()
#     print(queue)
    
# deques(deque(['Maths','English','Physics','Chemistry','Computer']))

# The del statement
a=['apple','orange','mango','banana','pear','date']
del a[4]
print(a)
    
    