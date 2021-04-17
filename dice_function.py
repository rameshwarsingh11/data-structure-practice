# Dice function in python. The dice rolls for random numbers between 1 to 7. Simulate it to a 5 number dice only.
from random import randint


def dice_function():
  return randint(1, 7)


def convert7to5():
  roll = 7

  while roll > 5:
      # Keep rolling until your roll is above 5 to simulate the dice for 5 numbers only.
    roll = dice_function()
    print('Dice function produced a roll of', roll)
  print('Your roll is below : :')
  return roll


print(convert7to5())
