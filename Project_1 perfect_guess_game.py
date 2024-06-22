import random
a = -1
n = random.randint(1,100)

guess = 1 

while(a != n):
    guess += 1
    a = int(input('guess a number'))
    if(a>n):
        print('lower number pls')
    else:
        print('higher number pls')


    

       


print(f'''you have guessed correctly in {guess} attempt
      if you guessed in less than 10 attemps well played
      if you guessed in less than 20 attempts acceptable
      but if you guessed in more than 20 attempts, you are noob''')


