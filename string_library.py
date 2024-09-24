'''
String Libraries
'''

# 1)Slicing
# slicing = lambda s:s[0][3:7]
# print(slicing(s=['Pyhton']))

# # 2)strip
# strip = lambda s:s.strip( "HE")
# print(strip(s="HELLO"))

# # 3)lstrip (left-strip)
# lstrip = lambda s:s.lstrip(" Python ")
# print(lstrip(s="  Python is a high-level language "))

# # 4)rstrip (right-strip)
# right = lambda s:s.rstrip("level language**")
# print(right(s="**Python is high-level language**"))

# #  strip with character
# char = lambda s:s.strip("('####$$$')")
# print(char(s="####Python$$$"))

# # 5)removeprefix
# prefix = lambda s:s.removeprefix(":) Welcome")
# print(prefix(s=":) Welcome Back Home :) "))

# # 6)removesuffix
# suffix = lambda s:s.removesuffix("Home :) ")
# print(suffix(s=":) Welcome Back Home :) "))

# # 7)replace
# place = lambda s:s.replace("Gentleman","Ladies")
# print(place(s="Ladies and Gentleman"))

import re
s1 = lambda s: re.sub("\s+", "=", s)
print(s1(s="Today    is sunday"))
                                                                     # import re
                                                                     # s1 = lambda s:re.sub(r"\s+"  "=" , s)
                                                                     # print(s1(s="Today  is sunday"))


# # 9)split
# spilt = lambda s:s.split()
# print(spilt(s="Pyhton is a high-level language"))

# 10)rsplit with maxsplit
# rspilt = lambda s:s.rsplit()
# print(rspilt(s=" Pyhton is a high-level   language "))

# max = lambda s:s.rsplit(" ", maxsplit=2)
# print(max(s=" Pyhton is a high-level   language "))

# 11)join
# lists = lambda s:'  '.join(s)
# print(lists(s= ['Welcome',' back',' Home']))

# 12)upper()
# uppers = lambda s:s.upper()
# print(uppers(s="i love coffee"))

# 13)lower()
# lowers = lambda s:s.lower()
# print(lowers(s="I LOVE coFFEE"))

# 14)capitalize
# capital = lambda s:s.capitalize()
# print(capital(s="I LOVE COFFEE"))

# 15)islower()
# ilower = lambda s:s.islower()
# print(ilower(s="i love coffee"))

# 16)isupper()
# iupper = lambda s:s.isupper()
# print(iupper(s="i love coffee"))

# 17)isalpha , 18)isnumeric , 19)isalnum
# alpha = lambda s:s.isalpha() 
# print(alpha(s="COFFEE12"))

# 18)isnumeric
# numeric = lambda s:s.isnumeric()
# print(numeric(s="123456"))

# 19)isalnum
# num = lambda s:s.isalnum()
# print(num(s="2024sept"))

# 20)count()
# counts = lambda s:s.count("e")
# print(counts(s="Python is interpreted and high-level language."))

# 21)find()
# index = lambda s:s.find("o")
# print(index(s=" Welcome home "))

# 22)rfind()
# finds = lambda s:s.rfind('e')
# print(finds(s="I love coffee"))

# 23)startswith()
# start = lambda s:s.startswith("el")
# print(start(s="Welcome back"))

# # 24)endswith
# end = lambda s:s.endswith("ck")
# print(end(s="Welcome back"))

# 25)partition
# part = lambda s:s.partition(' ')
# print(part(s="I love coffee"))

# 26)center()
# centre = lambda s:s.center(40,'+')
# print(centre(s="I like chocolate"))

# # 27)ljust()
# ljusts = lambda s:s.ljust(40,'+')
# print(ljusts(s="I like chocolate"))

# 28)rjust
# rjusts = lambda s:s.rjust(40,'+')
# print(rjusts(s="I like chocolat"))

# 29)f-Strings
# number = 2
# strings = lambda s:s
# print(strings(f"Can I go {number} drink water ?"))


# 30)swapcase
# swap = lambda s:s.swapcase()
# print(swap(s="WELCOME Back"))

# 31)zfill()
# fill = lambda s:s.zfill(5)
# print(fill(s="+24"))


