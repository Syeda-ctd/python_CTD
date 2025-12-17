def make_hangman(secret_word):
    guesses = []
    
    def hangman_closure(letter):
        guesses.append(letter.lower())
        display = ""
        
        #build display word
        for char in secret_word.lower():
            if char in guesses:
                display += char
            else:
                display += "_"
        print(display)
        
        #check if all letters guessed
        return "_" not in display
    return hangman_closure     

# Game setup
secret = input("Enter the secret word: ")
play = make_hangman(secret)

# Keep guessing until word is complete
while True:
    guess = input("Guess a letter: ")
    if play(guess):
        print("🎉 You guessed the word!")
        break
 