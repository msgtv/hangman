import random


print('H A N G M A N')
while True:
    user_choice = ''
    while user_choice not in ('play', 'exit'):
        user_choice = input('Type "play" to play the game, "exit" to quit: ')
    if user_choice == 'play':
        WORDS = ('python', 'java', 'kotlin', 'javascript')
        word = random.choice(WORDS)
        secret_word = ['-' for _ in range(len(word))]
        other_letters = []
        lives = 8
        while lives > 0:
            print()
            print(''.join(secret_word))
            ent_letter = input("Input a letter: ")
            if len(ent_letter) != 1:
                print("You should input a single letter")
            elif ent_letter.isupper() or not ent_letter.isalpha():
                print("Please enter a lowercase English letter")
            elif ent_letter in other_letters or ent_letter in secret_word:
                print("You've already guessed this letter")
            else:
                if ent_letter not in set(word):
                    lives -= 1
                    if ent_letter not in set(word):
                        print("That letter doesn't appear in the word")
                        other_letters.append(ent_letter)
                else:
                    for i in range(len(word)):
                        if ent_letter == word[i]:
                            secret_word[i] = ent_letter
            if set(secret_word) == set(word):
                print(f'You guessed the word {"".join(secret_word)}!')
                print('You survived!\n')
                break
        else:
            print('You lost!\n')
    else:
        quit()
