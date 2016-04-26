"""
sources: http://stackoverflow.com/questions/306400/how-do-i-randomly-select-an-item-from-a-list-using-python, https://inventwithpython.com/chapter9.html, http://stackoverflow.com/questions/14667578/check-if-a-number-already-exist-in-a-list-in-python, mary feyrer, Glen Passow (game tester)
"""

import random
import string
a=string.ascii_lowercase
choose=int(input("Type '1' if you want to guess the word. Type '2' if you want the computer to guess your word. "))

if choose==2:
    newword=input("What is your word? ")
    newword=newword.lower()
    l=len(newword) #count the number of letters
    
    word=[] #creating a list of letters in newword
    for x in range(0,l):
        abc=newword[x]
        word.append(abc)
        
    letter1=random.choice(a)
    
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
        num=num+2
        print("Computer's guess = "+letter1+"   "+' '.join(guess) )
        
    time.sleep(1)

    while turns<7 and num>0:
        letter1=random.choice(a)
        
        for x in range(0,l):
            if letter1==word[x]:
               guess[x]=letter1
            elif guess[x] not in a:
                guess[x]='_'
        
        if letter1 not in word:
            turns=turns+1
        print("Computer's guess = "+letter1+"   "+' '.join(guess) )
        
        time.sleep(1)
        
        if turns==5:
            print("You stumped the computer!")
        
        if word==guess:
            print("The computer guessed your word.")
            turns=100

elif choose==1:
    words = ['giraffe', 'hangman', 'tulip', 'purple', 'petunia', 'delivery', 'extraneous', 'plywood', 'highway', 'pullover']
        
    newword=random.choice(words) #randomly select word
    l=len(newword) #count the number of letters
    
    word=[] #creating a list of letters in newword
    for x in range(0,l):
        abc=newword[x]
        word.append(abc)
        
    letter1=input("number of spaces = "+str(l)+". After seven wrong guesses, you lose. First guess? ") #first letter guess
    while letter1 not in a:
        letter1=input("Invalid input. Please guess a lowercase letter.") 
        
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
        num=num+2

    while turns<7 and num>0:
        
        while letter1 not in a:
            letter1=input("Invalid input. Please guess a lowercase letter.") 
        
        letter1=input(' '.join(guess)+" Number of wrong guesses = "+str(turns)+". Next guess?")
        
        for x in range(0,l):
            if letter1==word[x]:
               guess[x]=letter1
            elif guess[x] not in a:
                guess[x]='_'
        
        if letter1 not in word:
            turns=turns+1
        
        
        if turns==5:
            print("The word was "+newword+". Game over.")
        
        if word==guess:
            print("The word is "+newword+". You won!")
            turns=100
    
else:
    print("Invalid input. Start over.")


    
