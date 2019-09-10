import random


def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns:
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word




def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''

    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    blanks = ''
    for letter in secret_word:  #converts secret_word string into _
        if letter in letters_guessed:
            blanks += letter
        else:
            blanks += "_"
    return blanks



def check_used_letters(used_letters):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    wrong = ''
    for letter in alphabet:
        if letter not in secret_word:
            wrong += letter
    print(f"These letters have been guessed {wrong}")

def is_guess_in_word(guess, secret_word):
    # checks to see if the letter guessed is in the secret word
    return guess in secret_word

def letter_guess():
    guess = ''
    while len(guess) == 0:
        print(f'The secret word is {secret_word}')
        guess = input('Guess a letter: ')

    return guess


def spaceman(secret_word):
    used_letters = []
    correct_letters = []
    guessesRemaining = 7
    while guessesRemaining > 0:
        guess = letter_guess()

        if guess not in used_letters:
            used_letters.append(guess)

        if is_guess_in_word(guess, secret_word):
            correct_letters.append(guess)
            blanks = get_guessed_word(secret_word, correct_letters)
            if blanks == secret_word:
                print(f'You guessed {blanks} correctly you WIN!!!')
                return
            print(f'Guessed word so far {blanks}')

        else:
            guessesRemaining -= 1
            if guessesRemaining == 0:
                print(f'You have 0 guesses remaining you lose. the word was {secret_word}')
                return
            print('Sorry, your guess was not in the word, try again!')
            print(f'You have {guessesRemaining} incorrect guesses left')
            blanks = get_guessed_word(secret_word, correct_letters)
            print(f'Guessed word so far {blanks}')
        check_used_letters(used_letters)

secret_word = load_word()
spaceman(secret_word)
