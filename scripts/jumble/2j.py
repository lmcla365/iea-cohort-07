import random

#open list of possible words
words_file = open("./words", "r")
words = words_file.readlines()

#chose a random word
selected_word = random.choice(words).strip()
#print(selected_word) 

#set selected word to list
word_list = list(selected_word)

print('''\nTry to guess the word from the jumbled letters. The order changes every time.\nYou can give up at by typing UNCLE. Good luck.''')

while True:
    random.shuffle(word_list) #jumble letters
    print("\nCan you unscramble the word?")
    print(''.join(word_list)) #print jumbled letters as string
    guess = input("Take a guess: ") 
    if guess == selected_word:
        print("You got it!!! The word is", selected_word)
        break
    if guess == 'UNCLE':
        print("\nQuitter! The word was",selected_word)
        break
