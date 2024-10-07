# Built-in Dictionary Methods

# d.clear()
# def cleans(months):
#     print(months)
#     months.clear()
#     print(months)

# cleans({
#     1:"monday",
#     2:"tuesday",
#     3:"wednesady",
#     4:'thursady',
#     5:'friday',
#     6:'saturday',
#     7:'sunday'})   

# d.get(<key>[, <default>])
# def gets(brands):
#     print(brands)
#     print(brands.get(4))
    
# gets({1:'addias',2:'gucci',3:'levis',4:'celine',5:'ck'})    

# d.items()
# def item(fruits):
#     print(list(fruits))
#     print(list(fruits)[0][3])

    
# item({
#     'mango':2,
#     'orange':4,
#     'pear':6,
#     'date':8
# })    

# d.keys()
# def key(days):
#     print(days)
#     print(days.keys())
    
# key({
#     1:'monday',
#     2:'tuseday',
#     3:'wednesday',
#     4:'thursdau',
#     5:'friday',
#     6:'saturday',
#     7:'sunday',
# })    

# d.values()
# def day(days):
#     print(days)
#     print(days.values())
    
# day({
#     1:'monday',
#     2:'tuseday',
#     3:'wednesday',
#     4:'thursdau',
#     5:'friday',
#     6:'saturday',
#     7:'sunday',
# })    

# d.pop(<key>[, <default>])
# def pops(clothes):
#     print(clothes.pop(2))
#     print(clothes)
    
# pops({
#     1:'shirts',
#     2:'skirts',
#     3:'pants',
#     4:'coat',
#     5:'t-shirt',
#     6:'socks',
#     7:'scarf'
# })    

# d.popitem()
# def item(cloth):
#     cloth.popitem()
#     print(cloth)
    
# item({
#     1:'shirts',
#     2:'skirts',
#     3:'pants',
#     4:'coat',
#     5:'t-shirt',
#     6:'socks',
#     7:'scarf'
# })   

# d.update(<obj>)
def upto(month,months):
    print(month)
    month.update(months)
    print(month)
    
upto({
    1:'jan',
    2:'feb',
    3:'mar',
    4:'apr',
    5:'may',
    6:'june',
} , {
    7:'july',
    8:'aug',
    9:'sept',
    10:'oct',
    11:'nov',
    12:'dec',
})   