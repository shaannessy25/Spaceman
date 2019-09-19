from spaceman import *

def test_is_word_guessed ():
    assert is_word_guessed('hello', 'hello') == True
    assert is_word_guessed('hello', 'h') == False
    assert is_word_guessed('hello', 'hel') == False

def test_get_guessed_word ():
    assert get_guessed_word('hello',['h', 'e']) == "he_ _ _ "
    assert get_guessed_word('world', ['h', 'e', 's', 'q']) == '_ _ _ _ _ '
    assert get_guessed_word('world', ['h', 'e', 's', 'l']) == '_ _ _ l_ '

def test_is_guess_in_word ():
    assert is_guess_in_word('h', 'hello') == True
    assert is_guess_in_word('h', 'air') == False
    assert is_guess_in_word('ell', 'hello') == True
    assert is_guess_in_word('ellr', 'hello') == False
