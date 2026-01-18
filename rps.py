import random

LINE = "\n–––––––––––––––––––––––––––––––––———––––––––––––"

class RockPaperScissors():

    def __init__(self):
        self.RULES = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

        self.human_score = 0
        self.computer_score = 0
        self.rounds = 0

    # ==================== LOGIC ====================
    def get_computer_choice(self):
        return random.choice(list(self.RULES.keys()))

    def get_human_choice(self):
        while True:
            choice = input("\nEnter your choice (rock/paper/scissors): ").strip().lower()

            if choice in self.RULES:
                break
            else:
                print("\nPlease enter a valid choice.")
        return choice

    def check_win(self, human_choice, computer_choice):
        if human_choice == computer_choice:
            return "draw"
        elif self.RULES[human_choice] == computer_choice:
            return "human"
        else:
            return "computer"

    def play(self):
        while self.rounds != 0:
            human = self.get_human_choice()
            computer = self.get_computer_choice()
            winner = self.check_win(human, computer)

            print(LINE)

            print(f'\nPlayer choice: {human}')
            print(f'Computer choice: {computer}')

            match winner:
                case "draw":
                    print("\nIt's a draw")
                case "human":
                    self.human_score += 1
                    print("\nPlayer won!")
                case "computer":
                    self.computer_score += 1
                    print("\nComputer won!")
                
            self.rounds -= 1
            print(self.get_score())
            print(f'Rounds left: {self.rounds}' if self.rounds != 0 else 'Game Over!')
             
    def start(self):
        while True:
            self.print_menu()
            self.play()
            print(LINE)
            if self.human_score > self.computer_score:
                print("\nPlayer won the game!")
            elif self.human_score < self.computer_score:
                print("\nComputer won the game!")
            else:
                print("\nPlayer and Computer tied.")
            print(self.get_score())
            print(LINE)

            if input("\nWould you want to play again? (y/n): ") != "y":
                break
            else:
                self.reset_game()

    def reset_game(self):
        self.human_score = 0
        self.computer_score = 0

    # ==================== UI ====================
    def get_score(self):
        return f'\nHUMAN: {self.human_score} | COMPUTER: {self.computer_score}'

    def print_menu(self):
        print(LINE)
        print("\nROCK PAPER SCISSORS")
        print("\nHow many rounds would you play against the computer?")
        while True:
            try:
                self.rounds = int(input("Rounds: "))
                break
            except ValueError:
                print("\nInvalid input. Please try again.\n")
        print(LINE)