import random

MAX_GUESSES = 5
START = 1
END = 20


def get_random_number():
    return random.randint(START, END)


class Game:

    def __init__(self):
        self._guesses = set()
        self._answer = get_random_number()
        self._win = False

    def guess(self):
        guess = input(f"Guess a number between {START} and {END}: ")

        if not guess:
            raise ValueError("Please enter a number")

        try:
            guess = int(guess)
        except ValueError:
            raise ValueError("Should be a number")

        if guess in self._guesses:
            raise ValueError("Already guessed")
        else:
            self._guesses.add(guess)

        if guess not in range(START, END + 1):
            raise ValueError(F"Not in range {START} to {END}")

        return guess

    def _check_guess(self, guess):
        if guess > self._answer:
            print(f"{guess} is too high")
            return False
        elif guess < self._answer:
            print(f"{guess} is too low")
            return False
        else:
            print(f"{guess} is correct!")
            self._win = True
            return True

    def __call__(self):
        while len(self._guesses) < MAX_GUESSES:
            try:
                guessed = self.guess()
                is_win = self._check_guess(guessed)
                if is_win:
                    print("You won!")
                    return
            except ValueError as ve:
                print(ve)
                continue

        print("You lost")
