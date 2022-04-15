#!/usr/bin/python3

import random

#open list of possible words
words_file = open("/home/catkinson2274/iea-cohort-07/scripts/jumble/wordlist", "r")
words = words_file.readlines()

#chose a random word
selected_word = random.choice(words).strip()
print(selected_word) 

#set selected word to list
word_list = list(selected_word)

#create some random incorrect messages
wrong_list = ["Nope!", "That's not the word we're looking for.", "This game is tough.", "Ummm. I don't think so.", "Keep guessing.", "¡Conjetura incorrecta!", "Think McFly!", "If at first you don't succeed...", "Don't forget. Guess UNCLE to quit", "Come on! That's not it.", "Hint: These are English words.", "If you play enough, you'll eventually get a three letter word. :-)", "There's a lesson here, and I'm not going to be the one to figure it out. - Rick Sanchez"]

print("\nTry to guess the word from the jumbled letters. The order changes every time.\nYou can give up at by typing UNCLE. Can you unscramble the word? Good luck!\n")

while True:
    random.shuffle(word_list) #jumble letters
    print(''.join(word_list)) #print jumbled letters as string
    guess = input("Take a guess: ").strip() 
    if guess == selected_word:
        print("\nYou got it!!! The word is", selected_word,"\n")
        break
    if guess == 'UNCLE':
        print("\nQuitter! The word was",selected_word,"\n")
        break
    else:
        wrong = random.choice(wrong_list) #assign random incorrect message
        print(wrong,"\n")
