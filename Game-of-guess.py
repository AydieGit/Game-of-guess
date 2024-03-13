import random
def random_number():
  random_number = random.randint(1,100)
  return random_number
random_number = random_number()
print(f"Welcome to the game of guess! \nI'm thinking of a number between 1 and 100. \nThe corrent number is {random_number}")
difficulty_level = input("Type 'easy' or 'hard': ")
def game():
  game_status = True
  number_of_lives = 0
  while game_status:
    if difficulty_level == "easy":
      number_of_lives = 10
    elif difficulty_level == "hard":
      number_of_lives = 5
    
    while number_of_lives != 0:
      guess = int(input(f"You have {number_of_lives} attemps reamining to guess the number. \nMake a guess: "))
      print(guess)
      if guess == random_number:
        print(f"You got it! The answer was {random_number}")
        break
      elif guess < random_number:
        print(f"Too low. \nGuess again.")
        number_of_lives -= 1
      elif guess > random_number:
        print(f"Too high. \nGuess again.")
        number_of_lives -= 1
      if number_of_lives == 0:
        print("You've run out of guesses, you lose.")
        game_status = False
    break
game()
