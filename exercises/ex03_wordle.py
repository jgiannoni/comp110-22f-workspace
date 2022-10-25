"""feiwvbiefbwv."""

__author__ = "730529967"


def main() -> None:
    """Main."""
    turn: int = 1
    word = "quiet"
    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(word))
        print(emojified(guess, word))
        if guess == word:
            print(f"You won in {turn}/6 turns!")
            break
        turn += 1
    if guess != word:
        print("X/6 - Sorry, try again tomorrow!")


def contains_char(word: str, char: str) -> bool:
    """If char in word."""
    assert len(char) == 1
    if char in word:
        return True
    else:
        return False
# this tells us if the character is in the word and will allow us to find if the yellow emoji is needed


# from exercises.ex03_wordle import contains_char

white: str = "\U00002B1C"
green: str = "\U0001F7E9"
yellow: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Emojis."""
    assert len(guess) == len(secret)
    emojis: str = ""
    i: int = 0
    while i < len(secret):
        if guess[i] == secret[i]:
            emojis = emojis + green
        elif contains_char(secret, guess[i]):
            emojis = emojis + yellow
        else:
            emojis = emojis + white
        i += 1
    return emojis


# from exercises.ex03_wordle import emojified


def input_guess(number: int) -> str:
    """Guess a word of certain length."""
    guesss = input("Enter a " + str(number) + " character word: ")
    while len(guesss) != number:
        guesss = input("That wasn't " + str(number) + " chars! Try again: ")
    return guesss

# from exercises.ex03_wordle import input_guess


if __name__ == "__main__":
    main()
