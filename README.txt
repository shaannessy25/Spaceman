secret_word = load_word()

The secret word call the load word function. The load word function opens a text
file, imports the words, and arranges the words into a list. From the list the
words a random chosen and split into individual letters.

spaceman(secret_word)

calls spaceman function and uses secret_word as its passing parameter.

the spaceman function is the main function of our code where the user will
play the game.

spaceman function will do this:
  Greet the user
  store letters used in a list
  store correct letters used in a list
  Guess count = 7

  while the guess count is greater than 0 do this:
    take the user guesses and perform checks with letter guess function.

  if the user guessed letter is not in used letter then add letter to list

  if the user guessed letter is correct then add letter to correct letters list
  

letter_guess:
  while the guess is a valid input display the length of the secret word
