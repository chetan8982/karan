# what is function in python.
# every function has their own purpose.
# function is a block of instruction(code) which execute inside its own block.
# function


#how define function in python.
#def abc():
# a=21
# b=10
# c=a+b
# print(c)
#add() # function call

# 













# divide in four function:
#1. take nothing return nothing.
#2. take nothing return something.
#2.take something return nothing.
#4.take something return something.

# parameters(para)n and arguments(args).
#positional parameter/arguments
# default parameter

# def add(a,b):
#     c= a+b
#     print(c)
# add(10,20)

# def table_print(n):
#     for i in range(1,11):
#         print(f"{n} x {i} = {n*i}")
# n=2
# table_print(n)

# function for addition
# def add(a=0,b=0):
#     c=a+b
#     print("add",c)
# add(14,34)

# function for subtraction
# def sub(a=0,b=0):
#     c=a-b
#     print("sub= ",c)
# sub(15,10)

# def add(a,b):
#     c=a+b
#     return c
# res= add(3,4)
# print(res)

# def add(a,b):
#     return a+b
# res=add(20,10)

# def sub(c,res):
#     return res - c 
# d=sub(90,res)
# print(d)

# def sub(a,b):
#     return a-b
# res=sub(20,19)

# def add(c,res):
#     return c+res
# v=add(13,res)
# print(v)

# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n -1)
# result= factorial(5)
# print(result)

#wap to check number pass by argument is ood or even.

# def even_odd(num):
#     if num % 2==0:
#         print("even")
#     else:
#         print("odd")
# even_odd(5)
    
#  wap a fu#nction which number is greter and two number is greter.
# def greter_number(num1,num2):
#     if num1>num2:
#         print(" a is greter than by b")
#     else:
#         print("a is smaller than by b")
# greter_number(5,6)
       

# waf to check characcter is vowel or consonant.
# num1=input("content= ")
# def check_vowels(text):
#     if text in "aeious":
#         print(f"This is vowels: {text}")
#     else:
#         print(f" this ia constant : {text}")
# check_text(user_input)

#waf to check is number completly divide by 2 and 3 and retur
#yes number is completly divide.
#no number is not completliy divide.


# def check_number(a):
#     if a%2==0 and a%3==0:
#         print(" it is completly divisible ")
#     else:
#         print("it is not  completly divisible ")
# user_input=25
# check_number(user_input)

# waf to return length of a string pass by user without using len().
def len_string(s):
    c=0
    for i in s:
        c=c+1
    return c
res=len_string("pythonbatch")
print(res)       


    
    

    
