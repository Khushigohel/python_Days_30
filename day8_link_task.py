##### oops #####
#### create the class and how  init mehod use and how to creae he bjec #####
class student:
    def __init__(self,name):
        self.name=name
    def printname(self):
        print(self.name)
s1=student('alice')
s1.printname()


class MotorBike:
  def __init__(self, brand, age):
    if(age <= 15):
      self.brand = brand
      self.age = age

  def start(self):
    print(f'starting {self.brand}....')

bullet = MotorBike('Royal Enfield Bullet',2)
bullet.start() # error. object is created only if age is less than or equals 15


#### Coding Exercise
'''The task is to create a class SoccerPlayer with name and goals attributes, then create 3 player objects and then using a 
function find out the maximum goals and print that.'''

class SoccerPlayer:
  def __init__(self, name, goals):
    self.name = name
    self.goals = goals


def calculateMaxGoals(*args):
  print(args)
  return max(*args)

messi = SoccerPlayer('messi', 10)
ronaldo = SoccerPlayer('ronaldo',22)
neymar = SoccerPlayer('neymar', 8)

max_goals = calculateMaxGoals(messi.goals, ronaldo.goals, neymar.goals)
print(f'The highest number of goals is {max_goals} goals')

#@classmethod and @staticmethod

class Calculator:
  def __init__(self,type):
    self.type = type

  @classmethod
  def calculate_sum(cls, num1, num2): 
        return num1 + num2
    # cls is just like self which needs to passed as 1st parameter

print(Calculator.calculate_sum(3,5)) # 8


## static method 
class Calculator:
  def __init__(self,type):
    self.type = type

  @staticmethod
  def multiply(num1, num2): 
        return num1 * num2
    # cls is just like self which needs to passed as 1st parameter

print(Calculator.multiply(3,5)) # 15



##### Inheritance   #####
class Player:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def run(self):
    return f'{self.name} is running'

class Cricketer(Player): # Syntax to inherit a class
  def catch_ball(self):
    return f'{self.name} Caught the ball'

class Batsman(Cricketer):
  def swing_bat(self):
    return f'what a shot by {self.name}'

player1 = Batsman('Virat Kohli', 31)

print(player1.run())
print(player1.catch_ball())
print(player1.swing_bat())

#### Encapulation ####

class Bank:
  def __init__(self,balance):
     self._balance=balance
  
  #getter method
  def get_balance(self):
    return self._balance
  
  #setter
  def def_deposit(self,amt):
    if amt > 0:
      self._balance += amt
    else:
      print("No Sufficient balance...")
      
account=Bank(40000)
account.def_deposit(3999)
print(f"your total amount is :{account.get_balance()}")


####### Abstraction
from abc import ABC,abstractmethod
class Animal(ABC):
  @abstractmethod
  def sound(self):
    pass
  def eat(self):
    print("Animal can be eat grass....")
    
class Dog(Animal):
  def sound(self):
    print("It is Dog i can be sund is  bho bho...")

obj=Dog()
obj.sound()
obj.eat()


#### super######
class Parent:
  def __init__(self,fname,lname):
    self.fname=fname
    self.lname=lname
  
  def property1(self):
    print("Here define he paren propery..")

class Child(Parent):
  def __init__(self,fname,lname,value):
    super().__init__(fname,lname)
    self.grandParent=value
    
  def welcome(self):
    print(f"hello {self.fname} and {self.lname}")
  
obj=Child("Khushi","Gohel",2000)
obj.welcome()
obj.property1()



#####dundur mehd 
class Sentence:
  words = []

  def add_word(self, word):
    self.words.append(word)

  def __len__(self):
    return len(self.words)

new_sentence = Sentence()
new_sentence.add_word('Hello')
new_sentence.add_word('World')
print(len(new_sentence))

##### Method Resolution Order #####
class Employee:
  secret_code = 'secret'

class Manager(Employee):
  secret_code = 'm123'

class Accountant(Employee):
  secret_code = 'a123'

class Owner(Accountant,Manager):
  pass

person = Owner()
print(person.secret_code) # a12
print(Owner.mro())