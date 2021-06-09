'''
Modules enable us to split parts of our program in different files for easier maintenance and better performance.
A module is a file consisting of Python code. It can define functions, classes, and variables, and can also include runnable code.
functions are one of the main building blocks of Python programming. 
Whenever we’ve typed something like len(x) or type(y) or even random.choice([1, 2, 3]), you’ve been using functions. 
'''

        # 1.) Function Creation 

def my_function():
  print("Hello from a function")
  
  
        # 2.)  Function  Call 

def my_function():
  print("Hello from a function")

my_function()

        # 3.) Function by arguments 

def my_function(fname):
  print(fname + " are good")

my_function("Emails")
my_function("Tablets")
my_function("mobiles")


        # 4.) Functions by Arbitrary Arguments, *args
        
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


        # 5.) Functions by Default Parameter Value
        
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


        # 6.) Return type functions
        
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

