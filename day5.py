#functions

#def
def greet():
    print("Hello!")

greet()   

#parameters
def greet(name):
    print("Hello, " + name + "!")

greet("Raja")  

#return

def add(a, b):
    return a + b

result = add(5, 3)
print(result)  

#local variable

def my_func():
    x = 10  
    print(x)

my_func()  

#global variable

y = 20  

def my_func2():
    print(y) 
 

my_func2()  
print(y)   



