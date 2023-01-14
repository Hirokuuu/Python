
def foo(x): #the argument is x 
    return x+5


def me(d): # anything with letter takes input 
    return d #this function returns d which is in the function "me"



hero = me(10) #me = 10 / d = 10 
help = foo(4)

#print(foo(4) + hero) prints out "me which is d"


def hello(): #defines this function / anything without letters take no input "argument"
    answer = input("What is your name? ") 
    response = "Hello " + answer #prints hello with anything you write Ex: like bob "Hello Bob"
    return response

#figma = hello()

#print(figma)

def add(x, y):
    z = x + y
    return z

you = add(5 , 2)

# print(you)

def empty(): #a function can be there but it doesnt have to take input or output 
  g = 6
  
def empty1(test): #it wont do anything with "test" 
  g = 6 
  print(test)
  return g 

# print(empty(), empty1("help")) #even if you attach a varible or string "empty1" will output none

# #empty1(5)

# print(empty())

x = 10 
y = 17

if x > y:
    print("x better then y")
elif x == y: # "==" compares x and y to see if they are the same 
    print("x is the same as y") 
else:
    print("y is better then x")


#define, argument, return 
#if statments are same as conditionals 
