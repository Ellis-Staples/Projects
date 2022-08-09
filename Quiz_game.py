print ('Welcome to my quiz!') # introduction

playing = input('Do you want to play? ')  #variable with user input

if playing.lower() != 'yes': # if true quits the game #any input is lowercase.
    quit()

print ('Okay, lets play!') # response
score = 0

answer = input('Which sea creature has three hearts? ') #First question
if answer.lower() == 'octopus':
    print ('Correct answer')
    score += 1
else:
    print ('Wrong answer')

answer = input('In the traditional rhyme, how many mice were blind? ') #Second question 
if answer == '3':
    print ('Correct answer')
    score += 1
else:
    print ('Wrong answer')

answer = input('How many bones does an adult human have? ') #Third question
if answer == '206':
    print ('Correct answer')
    score += 1
else:
    print ('Wrong answer')

answer = input('Water boils at 212 degrees on which temperature scale? ') #Fourth question
if answer.lower() == 'fahrenheit':
    print ('Correct answer')
    score += 1
else:
    print ('Wrong answer')

answer = input('What is the national flower of Wales? ') #Fifth question
if answer.lower() == 'daffodil':
    print ('Correct answer')
    score += 1
else:
    print ('Wrong answer')

print ('Your score was ' + str(score) + 'questions correct!') #string + converted int to string then + string

