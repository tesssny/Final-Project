"""
sources: http://stackoverflow.com/questions/306400/how-do-i-randomly-select-an-item-from-a-list-using-python, https://inventwithpython.com/chapter9.html, mary feyrer
"""

import random

words = ['giraffe', 'hangman', 'tulip', 'purple', 'petunia', 'delivery', 'extraneous', 'plywood', 'highway', 'pullover']

newword=random.choice(words) #randomly select word
l=len(newword) #count the number of letters

word=[] #creating a list of letters in newword
for x in range(0,l):
    abc=newword[x]
    word.append(abc)
    
l=str(len(newword)) #convert number of letters to a string so it can be printed

letter1=input("number of spaces="+l+"  ") #first letter guess



    
