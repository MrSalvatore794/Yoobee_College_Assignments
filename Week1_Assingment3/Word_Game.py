import random
import string

class WordGuessGame:
    """
    A class-based (OOP) version of the Word Guessing Game.
    This class encapsulates all game logic, state, and helper methods.
    """

    def __init__(self, max_lives=6):
        # Game configuration
        self.max_lives = max_lives

        # Game state variables
        self.secret_word = self.get_random_word()
        self.blanks = self.make_blanks(self.secret_word)
        self.lives = max_lives
        self.used_letters = set()


    # Utility Methods (Encapsulated)
    

    def get_random_word(self):
        """Return a random word from a predefined list."""
        words = [
            "python", "variable", "function", "iterator", "notebook",
            "pipeline", "dataset", "computer", "research", "analytics"
        ]
        return random.choice(words)

    def make_blanks(self, word):
        """Create a list of underscores representing hidden letters."""
        return ["_" for _ in word]

    def prompt_for_letter(self):
        """
        Ask the user for a valid letter.
        Ensures: single character, alphabetic, not used before.
        """
        while True:
            guess = input("Guess a letter: ").strip().lower()

            # Validate input
            if len(guess) != 1 or guess not in string.ascii_lowercase:
                print(" → Please enter a single A-Z letter.")
                continue

            if guess in self.used_letters:
                print(" → You already tried that letter.")
                continue

            return guess

    def reveal_letters(self, letter):
        """
        Reveal all occurrences of the guessed letter in the secret word.
        Returns True if at least one letter was found.
        """
        found_any = False

        for i, ch in enumerate(self.secret_word):
            if ch == letter and self.blanks[i] == "_":
                self.blanks[i] = letter
                found_any = True

        return found_any

    def all_blanks_filled(self):
        """Check if the player has guessed the entire word."""
        return "_" not in self.blanks

    
    # Main Game Loop
    
    def play(self):
        """Run the main game loop."""
        print("\nWelcome to Word Guessing!")
        print(f"The word has {len(self.secret_word)} letters.")
        print(" ".join(self.blanks))

        while True:
            guess = self.prompt_for_letter()
            self.used_letters.add(guess)

            # Check if guess is correct
            if self.reveal_letters(guess):
                print("\nWell done! You found a letter.")
                print(" ".join(self.blanks))

                # Check if game is won
                if self.all_blanks_filled():
                    print("\nCongratulations! You guessed the word!")
                    print(f"Word: {self.secret_word}")
                    print("GAME OVER")
                    break

            else:
                # Incorrect guess → lose a life
                self.lives -= 1
                print(f"\nNope. You lose a life. Lives left: {self.lives}")
                print(" ".join(self.blanks))

                # Check if game is lost
                if self.lives <= 0:
                    print("\nOut of lives!")
                    print(f"The word was: {self.secret_word}")
                    print("GAME OVER")
                    break

# Program Entry Point

if __name__ == "__main__":
    game = WordGuessGame(max_lives=6)
    game.play()
