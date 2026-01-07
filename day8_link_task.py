##### oops #####
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

#### Polymorphism ####
