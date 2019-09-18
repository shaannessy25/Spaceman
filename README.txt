Simplified Instructions:
  1. Display the amount of guess words and ask user to enter a letter
  2. Get user input and check to see if it is a letter
  3. If it is a letter check to see if the letter is in the secret words
  4. If letter is in secret word display letter
  5. If the letter is not in the secret word display answer is wrong and number
    attempts decrement by 1.
  6. If user guesses all of the correct letters then display "You Win"
  7. If user runs out of attempts display you've lost
  8. Ask the user if they want to play again



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


get_guessed_word:

convert the secret word string into '_' If the letter guessed is in the secret
word then display the letter in secret word.


is_word_guessed:

  for each letter in the secret word check to see if the letter is in the secret
  word. If yes then return true otherwise return False



is_guess_in_word
