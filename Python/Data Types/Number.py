#Numeric
# we need math module for the math functions

#types
x=2
y=4
c=2+3j #complex

print(type(c))


x="32"
print(x*2)

print(int(x)*3)
print(float(x)*3)

f=3.14
g=23

print(complex(f,g))

print(7//2) #floor

print(2**3) #expones

# rounding

print(abs(2-8)) # absolute
print(round(7/2)) # rounding

price= 35.789987
print(round(price))
print(round(price,3))

import math # for floor

print(math.floor(price))
print(math.ceil(price))

#intvstrun

print(math.trunc(price))

print(int(price))

#we can use int when we are using the value one time in a print or line because it changes the Value 
#trunc can be used if the something like price of product in the transaction to get a approximate price if we use in there it would cost a eg:3.50 for this .50 of amount of every transaction

#random

import random

print(random.random())
print(random.randint(1,99)) #range


#validation

#Whole number or not
x=7.0
y=7.1
print(x.is_integer())
print(y.is_integer())

print("*"*5)
#check if number are truly whole floats with 0 just be from file exports so that we can change them to integer

x=40.4
print(isinstance(x,int))
print(isinstance(x,float)) # checking whether x is integer
y=98
print(isinstance(y,int))


number=random.randint(1,100)

if(number%2 ==0):
    print(f"Number is a even number {number}")
else:
    print(f"Number is a odd number {number}")




