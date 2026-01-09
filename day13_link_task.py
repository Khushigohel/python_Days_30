#### Decoretor  ######
def multiplier(num1, num2):
  return num1 * num2

some_variable = multiplier # (a reference to the function is created)

del multiplier # (deletes the function)

print(some_variable(2,4)) # 8 (still able to call the function!)

#### Higher-Order Functions ####
def logger(func,args):
    print(f" the result f the passed funcin is {func(*args)}")
    
def sum(num1,num2):
    return num1 + num2

logger(sum,(1,2))


#### custom decorator ###
def statement(func):
    '''
        A decorator function which accepts a function
        and then wraps some goodness into it and
        returns it back!
    '''
    def wrapper():
        func()
        print(" you are under 18..")
    return wrapper
@statement
def layment():
    print('I am just a layman')

layment()