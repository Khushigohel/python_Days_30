#### Try except block ####

try:
    
    age = int(input('Enter your age : '))
    if age > 18:
        print('You are an adult')
    else:
        print('You are a minor')
except:
    print("Invalid value provided")
    
##### try,except with else blck
try:
    if age > 18:
        print('You are an adult')
    else:
        print('You are a minor')
except:
    print("Invalid value provided")
else:
    print("It is execute when he r block no error occur...")

#### Try with finally blck
try:
  age = int(input('Enter your age : '))
  if age > 18:
    print('You are an adult')
  else:
    print('You are a minor')
except:
  print('Invalid value provided')
finally:
  print('Sendiing dummy log to server')
  

from functools import reduce

def calc_average(number_list):
    '''
    accepts a list of numbers and returns average
    '''
    try:
        sum = reduce(lambda acc, curr: acc + curr, number_list)
        average = sum/len(number_list)
        return average
    except TypeError:
         print('Only a list of numbers is valid')
print(calc_average([1,2,3,4,5])) # 3.0
