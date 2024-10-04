# task :
# addition , ubractin and multiplication  of ararys :
# explore the arrasy and numpy arrasy 
# copy of ararsy    


# Addition of arrays 
import numpy as np

a = np.array([1,2,3])
b = np.array([1,2,3])
c = np.array([a+b])
print(c)   


a = np.array([10,20,30])
b = np.array([10,20,30])
c = np.array([a+b])
print(c) 

# Subtraction of array
x = np.array([20,40,60,80,100])
y = np.array([10,30,50,70,90])
minus=np.array([x-y])
print(minus)

# Multiplication of array
v = np.array([28,39,40,50])
w = np.array([23,43,76,78])
z = np.array([v*w])
print(z)

# copy of array
d=np.array([2.1,3.15,68.70,89.09])
f=np.array([12.34,45.65,1.6,23.45])
e=np.array([d,f])
print(e)