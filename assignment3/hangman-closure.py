# Function that returns the hangman closure
def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        nonlocal guesses
        letter = letter.lower()  # optional: make it case-insensitive
        if letter not in guesses:
            guesses.append(letter)

        # Build the display word with underscores
        displayed = "".join([c if c in guesses else "_" for c in secret_word.lower()])
        print(displayed)

        # Return True if all letters guessed, False otherwise
        return all(c in guesses for c in secret_word.lower())

    return hangman_closure


# ---------- Mainline: Hangman Game ----------
if __name__ == "__main__":
    secret_word = input("Enter the secret word: ").strip()
    game = make_hangman(secret_word)

    print("\nLet's start the game!")
    finished = False

    while not finished:
        guess = input("Guess a letter: ").strip()
        if len(guess) != 1:
            print("Please enter only one letter.")
            continue
        finished = game(guess)

    print(f"Congratulations! You guessed the word '{secret_word}'!")