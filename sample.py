
# candies={1:{"a","b","c"},3:[1,2,3]}
# new_candies=candies.copy()
# new_candies[3]=[1,2]
# print(cmp (new_candies,candies))
# print(type(candies))
# for i in candies:
#     print(candies[i])

# class Employee:  
#     # class variable   
#     salary=31000  
#     def __init__(self, name, department):  
#         # Instance variable  
#         self.name = name  
#         self.department = department  
  
#     # instance method to access instance variable  
#     def show(self):  
#         print('Name:', self.name, 'Department:', self.department, 'Salary:', Employee.salary)  
#     def hello():
#         print('Hello wORLD')
#     def change_salary(cls, salary):  
#         cls.salary = salary  
#     def show_salary(cls):
#         print(cls.salary)
# obj = Employee('Craig', 'IT') 
# obj.show_salary()
# obj.change_salary(45000)
# Employee.hello()


# # generator function that yields counting from 0 to n
# def count():
#     for i in range(0, 10+1):
#         yield i
# def gen_func():
#     yield 'hello'
#     yield 2
# # now calling generator function, gen_obj is termed as generator object       
# gen_obj = gen_func() 
# # returns the element
# for i in gen_obj:
#     print(i)


# def divide(x,y):  
#     print(x/y)  
# def outer_div(func):  
#     def inner(x,y):  
#         if(x<y):  
#             x,y = y,x  
#             return func(x,y)  
#     return inner  
# divide1 = outer_div(divide)  
# divide1(2,4)


# def outer_div(func):  
#     def inner():  
#         # if(x<y):  
#         #    x,y = y,x  
#         return func(4,7)  
#     return inner()  
# # syntax of generator  
# @outer_div  
# def divide(x,y):  
#      print(x/y)  

# def do_twice(func):
#     def inner_twice()):
#         print()
#         func()
#         func()
#     return inner_twice

# @do_twice
# def print_hello(x,y):
#     print("Hello"+str(x+y))

# def do_twice(func):
#     def inner_twice(x,y):
#         func(x,y)
#         func(x,y)
#     return inner_twice

# @do_twice
# def print_hello(x,y):
#     print("Hello"+str(x+y))

# print_hello(4,5)

# def do_twice(func):  
#     def wrapper_function(*args,**kwargs):  
#         func(*args,**kwargs)  
#         func(*args,**kwargs)  
#     return wrapper_function 


# @do_twice  
# def return_greeting(name):  
#      print("We are created greeting")  
#      return 8 
# hi_adam = return_greeting("Adam")

# memory = {}
# def memoize_factorial(f):
     
    # This inner function has access to memory
    # and 'f'
#     def inner(num):
#         # print('helloworld')
#         if num not in memory:
#             memory[num] = f(num)
#             print('result saved in memory')
#         else:
#             print('returning result from saved memory')
#         return memory[num]
 
#     return inner
     
# @memoize_factorial
# def facto(num):
#     if num == 1:
#         return 1
#     else:
#         return num * facto(num-1)
# print(facto(5))
# print(facto(5))

# help(range)


# from functools import *
  
# # A normal function
# def add(a, b, c):
#     return 100 * a + 10 * b + c
  
# # A partial function with b = 1 and c = 2
# add_part = partial(add,2,3)
# print(add_part(5))
# def outerFunction(text):
    
 
#     def innerFunction():
#         # text="hello"
#         print(text)
 
#     # Note we are returning function
#     # WITHOUT parenthesis
#     return innerFunction 
 
# if __name__ == '__main__':
#     myFunction = outerFunction('Hey!')
#     myFunction()


# Python3 program for demonstrating
# coroutine execution
 
def print_name(prefix):
    print("Searching prefix:{}".format(prefix))
    while True:
        name=(yield)
        if prefix in name:
            print(name)
 
# calling coroutine, nothing will happen
corou = print_name("Dear")
 
# This will start execution of coroutine and
# Prints first line "Searching prefix..."
# and advance execution to the first yield expression
corou.__next__()
corou.send('Atul Dear')
 
