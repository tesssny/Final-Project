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
for x in range(0,l-1):
    abc=newword[x]
    word.append(abc)
    
l=str(len(newword)) #convert number of letters to a string so it can be printed

letter1=input("number of spaces = "+l+". On the fourth wrong guess, you lose. First guess? ") #first letter guess

turns=0
while turns<4:
    l=int(l)
    guess=[]
    for x in range(0,l-1):
        if letter1==word[x]:
            guess.append(letter1)
        elif guess[x] not in a:
            guess.append('_')
    if letter1 not in word:
        turns=turns+1
    letter1=input(guess+" Number of wrong guesses = "+turns+". Next guess?")
    
    if turns==4:
        print("Game Over")


    
