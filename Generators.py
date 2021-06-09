''' 
 A generator-function is defined like a normal function, but whenever it needs to generate a value,it does so with the yield keyword rather than return. 
 If the body of a def contains yield, the function automatically becomes a generator function.
'''

          # 1.) A Python program to demonstrate use of generator object with next() 
  
# A generator function
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3
   
# x is a generator object

x = simpleGeneratorFun()
  
# Iterating over the generator object using next

print(x.next())      # In Python 3, __next__()
print(x.next())
print(x.next())

Output : 
1
2
3

          # 2.)  A simple generator for Fibonacci Numbers
  
def fib(limit):
      
    # Initialize first two Fibonacci Numbers 
    a, b = 0, 1
  
    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b
  
# Create a generator object
x = fib(5)

# Iterating over the generator object using for
# in loop.
print("\nUsing for in loop")
for i in fib(5): 
    print(i)
    
 Output : 
  0
  1
  1
  2
  3
  
  
  
            # 3.)  A simple generator function
    
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n
 
