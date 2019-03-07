import random

number = (random.randint(1,10))
#print(number) #delete this comment so you can cheat.
guessTaken = 0
totGuess = 3
print("you have 3 chance. Guess the number between 1 and 10")



while guessTaken < 6:
  guess = int(input("Take a guess: "))
  guessTaken = guessTaken + 1
  guessLeft = totGuess - guessTaken
  if guess == number:
    print("your guess is right")
    break#stops the loop
  elif guess < number :
    print("your guess is low")
    print ("you have ", guessLeft, " guess left")
  elif guess > number :
    print("your guess is high")
    print ("you have ", guessLeft, " guess left")
