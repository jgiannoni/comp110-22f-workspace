"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730529967"

word: str = input("Enter a 5-character word: ")

if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

guess: str = input("Enter a single character: ")

if len(guess) != 1:
    print("Error: Character must be a single character.")
    exit()
        
print("Searching for " + (guess) + " in " + (word))


num_matches: int = 0

if guess == word[0]:
    num_matches = num_matches + 1
    print(guess + " found at index 0")
if guess == word[1]:
    num_matches = num_matches + 1
    print(guess + " found at index 1")
if guess == word[2]:
    num_matches = num_matches + 1
    print(guess + " found at index 2")
if guess == word[3]:
    num_matches = num_matches + 1
    print(guess + " found at index 3")
if guess == word[4]:
    num_matches = num_matches + 1
    print(guess + " found at index 4")

if num_matches == 0:
    print("No instances of " + guess + " found in " + word)
if num_matches == 1:
    print("1 instance of " + guess + " found in " + word)
if num_matches == 2:
    print("2 instances of " + guess + " found in " + word)
if num_matches == 3:
    print("3 instances of " + guess + " found in " + word)
if num_matches == 4:
    print("4 instances of " + guess + " found in " + word)
if num_matches == 5:
    print("5 instances of " + guess + " found in " + word)