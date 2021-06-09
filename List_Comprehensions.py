'''
List comprehension offers a shorter syntax when we want to create a new list based on the values of an existing list.
'''

          # 1.) 
  
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

          # 2.) to print items containing 'a' in one line 
  
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

          # 3.) to print items of list 
  
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

          #4.) to check item in list
  
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  
           # 5.) Append list items 
    
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
    
    
    

