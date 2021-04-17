# Simulate a 7 sided dice from a 5 sided dice.
from random import randint


def dice5():
  return randint(1, 5)


def convert5to7():

  while True:

    # Roll the dice twice
    roll_1 = dice5()
    roll_2 = dice5()

    # Keep the range between 1 and 20
    num = ((roll_1 - 1)*5) + (roll_2)

    if num > 2:
      continue

    return num % 7 + 1


print(convert5to7())
