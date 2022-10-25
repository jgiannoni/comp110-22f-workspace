"""EX02 one shot wordle."""
__author__ = "730529967"

word = "python"

guess = input("What is your " + str(len(word)) + "-letter guess? ")

while len(guess) != len(word):
    guess = input("That was not " + str(len(word)) + " letters! Try again: ")

white: str = "\U00002B1C"
green: str = "\U0001F7E9"
yellow: str = "\U0001F7E8"

i: int = 0
emojis: str = ""

while i < len(word):

    if word[i] == guess[i]: 
        emojis = emojis + green
    elif guess[i] in word:
        emojis = emojis + yellow
    else:
        word[i] != guess[i]
        emojis = emojis + white
    i = i + 1
print(emojis)

if guess != word:      
    print("Not quite. Play again soon!")
if guess == word:
    print("Woo! You got it!")