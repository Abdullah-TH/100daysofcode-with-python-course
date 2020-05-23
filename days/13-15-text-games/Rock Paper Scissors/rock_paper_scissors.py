import random


class Role:

    def __init__(self, name):
        if name not in ["rock", "paper", "scissors"]:
            raise ValueError("name should be one of: rock, paper, scissors")
        self.name = name

    def can_defeat(self, other):
        if self.name == "rock":
            if other.name == "scissors":
                return True
            elif other.name == "paper":
                return False
            else:
                return None
        elif self.name == "scissors":
            if other.name == "paper":
                return True
            elif other.name == "rock":
                return False
            else:
                return None
        elif self.name == "paper":
            if other.name == "rock":
                return True
            elif other.name == "scissors":
                return False
            else:
                return None


class Player:

    def __init__(self, name):
        self.name = name


def game_loop():
    name = input("Please enter your name: ")
    player = Player(name)
    computer = Player("PythonBot")
    print(f"{player.name} VS {computer.name}!")
    print("Who ever scores 2 point will win!")
    print()
    player_score = 0
    computer_score = 0
    while True:
        role = input("Please choose rock, paper, or scissors: ")
        try:
            player_role = Role(role.lower())
            computer_role = Role(random.choice(["rock", "paper", "scissors"]))
            outcome = player_role.can_defeat(computer_role)
            print(f"{player.name} chooses {player_role.name}")
            print(f"{computer.name} chooses {computer_role.name}")
            if outcome is None:
                print("A tie!")
            elif outcome:
                print(f"{player.name} win!")
                player_score += 1
                print(f"{player.name} {player_score} and {computer.name} {computer_score}")
            else:
                print(f"{computer.name} win!")
                computer_score += 1
                print(f"{player.name} {player_score} and {computer.name} {computer_score}")

            print()

            if player_score == 2:
                print(f"{player.name} won the game!")
                break

            if computer_score == 2:
                print(f"{computer.name} won the game!")
                break

        except ValueError:
            print("You can choose only rock, paper, or scissors")
            continue


if __name__ == '__main__':
    game_loop()
