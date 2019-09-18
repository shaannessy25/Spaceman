from spaceman import *

def test_is_word_guessed ():
    assert is_word_guessed('hello', 'hello') == True
    assert is_word_guessed('hello', 'h') == False