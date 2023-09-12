print('Infinity Dice 🎲')
print()

def rollDice(sides):
  import random
  while True:
    a = random.randint(0, sides)
    print(f'You rolled {a}')
    print()
    b = input('Do you want to roll again?: ').lower()
    print()
    if b == 'yes':
      continue
    else:
      print('Bye! See you next time.😍')
      break
no_of_sides = int(input('How many sides do you want your dice to have?: '))
print()
rollDice(no_of_sides)