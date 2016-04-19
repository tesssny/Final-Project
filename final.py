"""
sources: http://stackoverflow.com/questions/306400/how-do-i-randomly-select-an-item-from-a-list-using-python, https://inventwithpython.com/chapter9.html, mary feyrer
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
    
l=str(len(newword)) #convert number of letters to a string so it can be printed

letter1=input("number of spaces="+l+" On the fourth wrong guess, you lose. First guess? ") #first letter guess

turns=0
while turns<4:
    guess=[]
    for x in word:
        if letter1==x:
            guess.append(x)
        else:
            guess.append('_')
        if x not in word:
            turns=turns+1
    
    if turns==4:
        print("Game Over")


    
