import random
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
word_list = ['adoam', 'probono', 'soccer']
chosen_word = random.choice(word_list)
chosen_word_masked = ['_' for char in chosen_word]
lives = 6
letters_used = []
while lives > 0:
    print(''.join(chosen_word_masked))
    guess = input("guess a letter\n").lower()
    if guess in letters_used:
        print("Letter already used, try other")
    else:
        letters_used.append(guess)
        for char in range(0, len(chosen_word)):
            if chosen_word[char] == guess:
                chosen_word_masked[char] = guess
        if guess not in chosen_word:
            lives -= 1
            print(HANGMANPICS[-lives-1])
            print("You have {} lifes left".format(lives))
        if '_' not in chosen_word_masked:
            lives = 0
            print("You win")