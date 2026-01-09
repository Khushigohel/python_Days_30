##### Generators
range_of_numbers = range(100) # a generator it isbuil in generator
for num in range_of_numbers: 
    print(num)
    
    
### hw  create the generator
def my_infinite_generator():
    num=0
    while True:
        yield num
        num+=1

res=my_infinite_generator()
print(next(res))
print(next(res))
print(next(res))
print(next(res))

### 
def my_infinite_generator(max):
    num=0
    while num < 3:
        yield num
        num+=1

res=my_infinite_generator(3)
print(next(res))
print(next(res))
print(next(res))
print(next(res))

#### fibonncci generator
def fibonacci_generator(num):
    a,b=0,1
    for item in range(num):
        yield a
        temp=a
        a=b
        b=temp + b
for num in fibonacci_generator(20):
    print(num)