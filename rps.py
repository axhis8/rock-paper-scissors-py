import random

class RockPaperScissors():

    LINE: str = "\n" + "–" * 35
    INVALID_INP: str = "\nInvalid input. Please try again."

    def __init__(self) -> None:
        self.RULES: dict[str: str] = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

        self.human_score: int = 0
        self.computer_score: int = 0
        self.rounds: int = 0

    # ==================== LOGIC ====================
    def get_computer_choice(self) -> str:
        return random.choice(list(self.RULES.keys()))

    def get_human_choice(self) -> str:
        while True:
            choice = input("\nEnter your choice (rock/paper/scissors): ").strip().lower()

            if choice in self.RULES:
                break
            else:
                print(self.INVALID_INP)
        return choice

    def check_win(self, human_choice: str, computer_choice: str) -> str:
        if human_choice == computer_choice:
            return "draw"
        elif self.RULES[human_choice] == computer_choice:
            return "human"
        else:
            return "computer"

    def play(self) -> None:
        while self.rounds != 0:
            human: str = self.get_human_choice()
            computer: str = self.get_computer_choice()
            winner: str = self.check_win(human, computer)

            print(self.LINE)

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
             
    def start(self) -> None:
        while True:
            self.print_menu()
            self.play()
            print(self.LINE)
            if self.human_score > self.computer_score:
                print("\nPlayer won the game!")
            elif self.human_score < self.computer_score:
                print("\nComputer won the game!")
            else:
                print("\nPlayer and Computer tied.")
            print(self.get_score())
            print(self.LINE)

            if input("\nWould you want to play again? (y/n): ") != "y":
                break
            else:
                self.reset_game()

    def reset_game(self) -> None:
        self.human_score = 0
        self.computer_score = 0

    # ==================== UI ====================
    def get_score(self) -> str:
        return f'\nHUMAN: {self.human_score} | COMPUTER: {self.computer_score}'

    def print_menu(self) -> None:
        print(self.LINE)
        print("\nROCK PAPER SCISSORS")
        print("\nHow many rounds would you play against the computer?")
        while True:
            try:
                self.rounds = int(input("Rounds: "))
                if self.rounds <= 0:
                    print(self.INVALID_INP)
                    continue
                else: 
                    break
            except ValueError:
                print(self.INVALID_INP)
        print(self.LINE)