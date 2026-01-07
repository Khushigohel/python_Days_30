####### Conditions & Loops I   ######
age = 33
if age <= 18:
    print("you can't vote")
else:
    print("you can  vote")
    
    
##### multiple condition check ####
is_adult = True
is_licensed = True

if is_adult and is_licensed:
    print("You are allowed to drive")
else:
    print('You are not allowed to drive')
    
    
######  Ternary Operator   #####
is_single=True
message='you can date' if is_single else "you can  not date"
print(message)


###### For Loops #####
for item in 'python':
    print(item)
for item in [1,2,3,4,5]: # List is iterable
    print(item,end='') # prints all numbers one at a time
    
for item in {1,2,3,4,5}: # Set is iterable
    print(item, end='')

for item in (1,2,3,4,5): # Tuple is iterable
    print(item,end='')
print()

###### Iterable #####
player = {
  'firstname': 'Virat',
  'lastname': 'Kohli',
  'role': 'captain'
}

for item in player:
    print(item)
for item in player.keys():
    print(item)
for key,value in player.items():
    print(key,' ',value)
for item in player.values():
    print(item)

###### range######
for item in range(10):
  print('python') # prints python 10 times

for item in range(0,10,1):
    print('hello') # prints hello 10 times

for item in range(0, 10, 2):
    print('hii') # prints hii 5 times 

for item in range(10, 0, -1):
    print(item) # prints in reverse order

print(list(range(10))) # generates a list of 10 items

#####  enumerate######
for key ,value  in enumerate(range(10)):
    print(f"key is :{key} value is :{value}")