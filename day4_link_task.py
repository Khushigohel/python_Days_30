#### list dataype ########
score=[44,45,66,77,55]
score.append(34)
print(score)

score.insert(2,74)
print(score)

score.extend([23]) 
print(score)

scores=score.append([44,66])
print(scores)

#Removing items from list (pop, remove, clear)
languages = ['C', 'C#', 'C++']
languages.pop()
print(languages) # ['C', 'C#']
languages.remove('C')
print(languages) # ['C#']
languages.clear()
print(languages) # []

#Getting index and counting (index, count)
alphabets = ['a', 'b', 'c']
print(alphabets.index('b'))
print(alphabets.count('a'))

#Sorting, reversing and copying lists
numbers = [1,4,6,3,2,5]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers_copy=numbers.copy()
print(numbers_copy)

#Some common list patterns
avengers = ['ironman', 'spiderman', 'antman', 'hulk']
rev=avengers[::-1]
print(rev)

merge_str=''.join(avengers)   #all string can be merge 
print(merge_str)

range_num=list(range(10))
print(range_num)


#list unpacking
first,second,third = ['tesla','ford','ferarri']
print(first) # tesla
print(second) # second
print(third) # ferarri

a,*others = [1,2,3,4,5] # remaining values are stored in others
print(a) # 1
print(others) # [2, 3, 4, 5]

first,*others,last= [12,3,4,5,6]
print(first) # 12
print(others) # ['3', '4', '5']
print(last) # 6




### Dictionaries #####
user={
    'Name':'Khushi',
    'age':12,
    'country':'india'
}
print(user['Name'])
print(user['country'])

user = {'name': 'Raghav', 'age': 20, 'country': 'India'}
print('name' in user.keys()) # True
print('gender' in user.keys()) # False
print('Raghav' in user.values()) # True

#dictionary methods are copy, clear, pop, update
cat = {
    'name': 'Tom',
    'greet': 'meow',
    'health': 100
}
cat_copy = cat.copy()
print(cat_copy) # {'name': 'Tom', 'greet': 'meow', 'health': 100}

cat.pop('name')
print(cat) # {'greet': 'meow', 'health': 100}

cat.clear()
print(cat) # {}

cat_copy.update({'name': 'Polo'})
print(cat_copy) # {'name': 'Polo', 'greet': 'meow', 'health': 100}
cat_copy.update({'color': 'Black'}) # adds key value if not present
print(cat_copy) # {'name': 'Polo', 'greet': 'meow', 'health': 100, 'color': 'Black'}


'''Tuples
Tuple data type is very similar to lists but they are immutable which means their value cannot be modified nor
they can be sorted like lists.'''

my_tuple=(1,2,3,4)
print(my_tuple)
print(1 in my_tuple)

colors = ('red', 'orange', 'blue', 'yellow')
print(colors[1:5])

my_color, *others=colors
print(my_color)
print(*others)

'''Sets
Sets are a data structure that stores an unordered collection of unique objects.'''
my_set={1,2,3,4,5}
print(my_set)

#This can be very helpful to remove say duplicate email addresses from a list of emails
emails = ['samantha@hey.com', 'rock@hey.com', 'samantha@hey.com']
email=set(emails)  #first convert into the set after covert into list
my_email=list(email)
print(my_email)


set_a = {1,2,3,4,5}
set_b = {4,5,6,7,8}
print(set_a.union(set_b)) # {1, 2, 3, 4, 5, 6, 7, 8}
print(set_a | set_b) # same as above just a compact syntax

print(set_a.intersection(set_b)) # {4, 5}
print(set_a & set_b) # same as above

set_a.discard(1)
print(set_a) # {2,3,4,5}
