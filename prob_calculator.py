import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **data):
    self.contents = []
    for key, value in data.items():
      for i in range (0,value):
        self.contents.append(key)

  
  def draw(self, numberOfDraws): 
    if(numberOfDraws>len(self.contents)):
      return(self.contents)
    else:  
      sample = random.sample(self.contents, numberOfDraws)
      for item in random.sample(self.contents, numberOfDraws):
        self.contents.remove(item)
      return(sample)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  M=0
  i=0
  temp = copy.copy(hat.contents)
  for test in range (0, num_experiments):
    T=1 #bool switch used for testing the values
    experiment = hat.draw(num_balls_drawn)
    hat.contents = copy.copy(temp)
    for key,value in expected_balls.items():
      for item in experiment:
        if(item == key):
          i = i + 1
      if (i < value):
        T = 0
      i=0
    if (T==1):
      M = M+1
  return(M/num_experiments)

# Pentru experiment de la 0 la num_experiments

  #Pentru fiecare pereche cheie(culoare) value(numer de bile) din expected_balls

    #Pentru fiecare element dintr-o extragere random de bile:
      #Daca elementul e egal cu cheia noastra, i++

  
