#####  Pure Functions #####
#  A pure function is a function that follows these two rules:   If provided the same input, it will return the same output always.
# It does not result in any side-effects.

def emoji_appender(list, emoji):
  '''
  Accepts a list and a emoji and 
  appends to every item of list
  '''
  new_list = []
  for item in list:
    new_list.append(str(item) + emoji)
  return new_list

print(emoji_appender([1,2,3], '😀')) # ['1😀', '2😀', '3😀']
print(emoji_appender(['alpha','beta','gamma'], '😀')) 


#### map function
list1=[1,2,3,4,5,6]
res=map(lambda x : x + 1,list1)
print(list(res))

#### filter
res=filter(lambda x: x % 2 == 0,list1)
print(list(res))

#### zip() The zip built-in function accepts multiple iterables and groups or zips them as tuples. 
username=['ALice','John']
email=['Alice@gmail.com','John@gmail.com']

users=list(zip(username,email))
print(users)

### reduce()
from functools import reduce

num=[1,2,3,4,5]
res=reduce(lambda x,y : x +y ,num)
print(res)


#### list comprihance
name = 'python'
new_list = [item for item in name] # here item can be any name

print(new_list)

#Dictionary Comprehension
brands = [
  {'name': 'Nike', 'category': 'shoes'},
  {'name': 'Reebok', 'category': 'shoes'},
  {'name': 'Tesla', 'category': 'cars'},
  {'name': 'Adidas', 'category': 'shoes'},
  ]

car_brands = [item for item in brands if item['category'] =='shoes']
print(car_brands) # filters out Tesla

#Set Comprehension

names = ['Rick', 'Alan', 'Rick', 'Mike']
new_set = {item for item in names}

print(new_set)


names = [
    'Harry', 'Johnny', 'Lewis', 'Harry', 'Buck', 'Nick', 'David', 'Harry',
    'Lewis', 'Michael'
]
duplicate_name=list(set([name for name in names if names.count(name) > 1]))
print(duplicate_name)

name=set(names)
print(name)