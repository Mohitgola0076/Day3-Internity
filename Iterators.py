'''
Iterator in python is an object that is used to iterate over iterable objects like lists, tuples, dicts, and sets.
The iterator object is initialized using the iter() method.
It uses the next() method for iteration.
This method raises a StopIteration to signal the end of the iteration.
'''

          # 1.) Iterating over a list
  
print("List Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
    print(i)
    
Output :
List Iteration
geeks
for
geeks

           # 2.) Iterating over a tuple (immutable)
  
print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
    print(i)
    
Output :
Tuple Iteration
geeks
for
geeks

           # 3.)  Iterating over a String
      
print("\nString Iteration")   
s = "Geeks"
for i in s :
    print(i)
      
Output : 
String Iteration
G
e
e
k
s

            # 4.) Iterating over dictionary
  
print("\nDictionary Iteration")  
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d :
    print("%s  %d" %(i, d[i]))
    
Output : 
Dictionary Iteration
xyz  123
abc  345
