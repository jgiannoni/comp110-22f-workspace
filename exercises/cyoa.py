"""EX06 Choose Your Own Adventur."""

__author__ = "730529967"


import random

points: int = 0
player: str = ()
quit: int = 0


def greet() -> None:
    """Greeting."""
    global player
    global points
    welcome_message: str = input("For this game you attempt to guess a random number in as few tries as possible. What is your name? ")
    player = welcome_message
    print(input("Welcome. What is your name?"))


SMILE_EMOJI: str = "\U0001f600"


def main() -> None:
    """Main."""
    global greet
    greet()
        
    def game_100() -> None:
        """Game 1-100."""
        global points
        global player
        global SMILE_EMOJI
        number: int = random.randint(1, 100)
        guess: int = int(input(f"Hello {player}!, guess a number 1-100 "))
        number_turns: int = 0 
        while guess != number:
            if guess > number:
                guess = int(input("Too high. Try again. "))
            if guess < number:
                guess = int(input("Too low. Try again. "))
            number_turns += 1
        print(f"Correct {SMILE_EMOJI}! you got it in {number_turns} tries!")
        if number_turns == 1:
            points = points + 10
            print("You earned 10 points!")
        elif number_turns == 2:
            points = points + 9
            print("You earned 9 points!")
        elif number_turns == 3:
            points = points + 8
            print("You earned 8 points!")
        elif number_turns == 4:
            points = points + 7
            print("You earned 7 points!")
        elif number_turns == 5:
            points = points + 6
            print("You earned 6 points!")
        elif number_turns == 6:
            points = points + 5
            print("You earned 5 points!")
        elif number_turns == 7:
            points = points + 4
            print("You earned 4 points!")
        elif number_turns == 8:
            points = points + 3
            print("You earned 3 points!")
        elif number_turns == 9:
            points = points + 2
            print("You earned 2 points!")
        elif number_turns == 10:
            points = points + 1
            print("You earned 1 points!")
        else:
            print("No points.")

    quit: int = 0

    def game_10(x: int) -> int:
        """Game with num 1=10."""
        global player
        s = random.randint(1, 10)
        num_tries: int = 0 
        points: int = 0 
        while x != s:
            if x > s:
                x = int(input(f"Too high {player}. Try again. "))
                num_tries += 1
            if x < s:
                x = int(input(f"Too low {player}. Try again. "))
                num_tries += 1
        if x == s:
            print(f"You got it in {num_tries} tries!")
        if num_tries == 1:
            points = points + 5
            print("You earned 5 points")
        elif num_tries == 2:
            points = points + 4
            print("You earned 4 points")
        elif num_tries == 3:
            points = points + 3
            print("You earned 3 points")
        elif num_tries == 4:
            points = points + 2
            print("You earned 2 points")
        else:
            print("No points")

        return num_tries

    while quit < 1:
        option = int(input("Option 1: Play Number Guess Option 2: Check how many points you have Option 3: Leave game. Input 1, 2, or 3 "))
        if option == 1:
            game_100()
        elif option == 2:
            game_10(int(input("Choose a number between 1 and 10")))
        elif option == 3:
            print(f"Game Over. You have earned {points} points!")
            quit += 1
        else:
            print("Please choose an option, 1, 2, or 3, and only input that number")


if __name__ == "__main__":
    main()