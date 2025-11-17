import random
import hangman_words
import hangman_art

print(hangman_art.logo)
lives = 6

chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
all_letters =[]

while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()


    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
            all_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        elif letter in all_letters:
            print(f"You have already guessed the letter: {guess}")
        else:
            display += "_"
    if guess in all_letters:
        print(f"You already guess this: {guess}")

    print("Word to guess: " + display)

    if guess not in chosen_word and guess not in all_letters:
        lives -= 1
    if guess not in chosen_word:
        all_letters.append(guess)

        if lives == 0:
            game_over = True

            print(f"***********IT WAS {chosen_word}!***********YOU LOSE**********************")


    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(hangman_art.stages[lives])
