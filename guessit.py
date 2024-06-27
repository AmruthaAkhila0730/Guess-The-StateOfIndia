import random

# List of words for the game
word_list = ["andhrapradesh", "arunachalpradesh", "assam", "bihar", "chhattisgarh", "gujarat", "haryana", "himachalpradesh", "jharkhand", "karnataka", "kerala", "madhyapradesh", "maharashtra", "manipur", "meghalaya", "mizoram", "nagaland", "odisha", "punjab", "rajasthan", "sikkim", "tamilnadu", "telangana", "tripura", "uttarpradesh", "uttarakhand", "westbengal"]

def get_partial_word(word):
    # Select 4 letters to show, excluding spaces (though spaces are already removed in the word list)
    indices_to_show = random.sample(range(len(word)), 4)
    partial_word = ['_'] * len(word)
    
    for index in indices_to_show:
        partial_word[index] = word[index]
    
    return ''.join(partial_word)

def word_guessing_game():
    word_to_guess = random.choice(word_list)
    partial_word = get_partial_word(word_to_guess)
    attempts = 3

    print("Welcome to the State Guessing Game!")
    print("In this game, you need to guess the name of an Indian state.")
    print("Please enter your guesses using lowercase letters only.")
    print(f"Guess the word: {partial_word}")

    while attempts > 0:
        user_guess = input("Enter your guess: ").strip().lower()

        if user_guess == word_to_guess:
            print(f"Congratulations! You guessed the word '{word_to_guess}' correctly!")
            return
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Wrong guess. You have {attempts} attempts left. Try again!")
            else:
                print(f"Sorry, you're out of attempts. The correct word was '{word_to_guess}'.")

if __name__ == "__main__":
    word_guessing_game()
