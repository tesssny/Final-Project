"""
sources: http://stackoverflow.com/questions/306400/how-do-i-randomly-select-an-item-from-a-list-using-python, https://inventwithpython.com/chapter9.html, http://stackoverflow.com/questions/14667578/check-if-a-number-already-exist-in-a-list-in-python, mary feyrer
"""

import random
import string
a=string.ascii_lowercase

words = ['giraffe', 'hangman', 'tulip', 'purple', 'petunia', 'delivery', 'extraneous', 'plywood', 'highway', 'pullover']

newword=random.choice(words) #randomly select word
l=len(newword) #count the number of letters

word=[] #creating a list of letters in newword
for x in range(0,l):
    abc=newword[x]
    word.append(abc)

letter1=input("number of spaces = "+str(l)+". After four wrong guesses, you lose. First guess? ") #first letter guess
letter1=letter1.lower() #making the guess lowercase

guess=[]
turns=0
num=0

while num<1:
    for x in range(0,l):
        if letter1==word[x]:
            guess.append(letter1)
        else:
            guess.append('_')
        if letter1 not in word:
            turns=turns+1
    num=num+1

while turns<4 and num>0:
    for x in range(0,l):
        if letter1==word[x]:
            guess.append(letter1)
        elif guess[x] not in a:
            guess.append('_')
    
    if letter1 not in word:
        turns=turns+1
    letter1=input(guess+" Number of wrong guesses = "+turns+". Next guess?")
    
    if turns==4:
        print("Game Over")
    
    if word==guess:
        print("The word is "+newword+". You won!")


    
