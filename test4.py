import random

def hangman():
    words = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    secret_word = random.choice(words)
    guessed_letters = []
    tries = 6

    while tries > 0:
        print()
        for letter in secret_word:
            if letter in guessed_letters:
                print(letter, end=' ')
            else:
                print('_', end=' ')
        
        guess = input("Enter a letter: ")
        guessed_letters.append(guess)
        
        if guess not in secret_word:
            tries -= 1
            print("Wrong guess!")
            print(f"You have {tries} tries left.")
        
        if set(guessed_letters) == set(secret_word):
            print("Congratulations! You guessed the word!")
            break
    
    if tries == 0:
        print("Sorry, you lost! The word was", secret_word)

hangman()
