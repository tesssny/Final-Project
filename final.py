"""
sources: http://stackoverflow.com/questions/306400/how-do-i-randomly-select-an-item-from-a-list-using-python, https://inventwithpython.com/chapter9.html, http://stackoverflow.com/questions/14667578/check-if-a-number-already-exist-in-a-list-in-python, mary feyrer, Glen Passow (game tester), http://stackoverflow.com/questions/7522533/how-can-i-turn-a-string-into-a-list-in-python, http://www.tutorialspoint.com/python/list_remove.htm, https://github.com/first20hours/google-10000-english, adam glueck, http://www.katrinerk.com/courses/python-worksheets/worksheet-reading-and-writing-files, http://www.datagenetics.com/blog/april12012/
"""
import random
import string
a=string.ascii_lowercase

choose=input("Type '1' if you want to guess the word. Type '2' if you want the computer to guess your word. Type '3' if you would like to play a two player game. ")

if choose=='2':
    newword=input("What is your word? ")
    newword=newword.lower()
    l=len(newword) #count the number of letters
    
    a2=list(a)
    common=('e','s','i','a','r','n','t','o','l','c','d','u','p','m','g','h','b','y','f','v','k','w','z','x','q','j')
    clength=len(common)
    letter=[]
    word=[] #creating a list of letters in newword
    guess=[]
    turns=0
    num=0
    
    for x in range(0,l):
        abc=newword[x]
        word.append(abc)
        if newword[x] not in a:
            print("Invalid input. Start over. ")
            turns=100
            num=0
            break
        else:
            if l>1:
                letter1="e"
                letter.append(letter1)
                num=1
          
            if l==1:
                letter1="a"
                letter.append(letter1)
                if letter1==word[x]:
                        guess.append(letter1)
                if letter1 not in word:
                    turns=turns+1
                    nextguess="i"
                    print("Computer's guess = "+letter1+"   "+' '.join(guess) )
                    letter1=nextguess
                    num=1
                if letter1 in word:
                    print("Computer's guess = "+letter1+"   "+' '.join(guess) )
                    print("The computer guessed your word.")
                    num=2
                    turns=100
                

    while num==1:
        for x in range(0,l):
            if letter1==word[x]:
                guess.append(letter1)
            else:
               guess.append('_')
        if letter1 not in word:
            turns=turns+1
        num=num+2
        print("Computer's guess = "+letter1+"   "+' '.join(guess) )
       
        if word==guess:
            print("The computer guessed your word.")
            turns=100

    while turns<10 and num>1:
        #for x in a2:
            #if x==letter1:
                #a2.remove(x)
        
        for x in range(1,clength):
            letter1=common[x]
        
            for x in range(0,l):
                if letter1==word[x]:
                   guess[x]=letter1
                elif guess[x] not in a:
                    guess[x]='_'
            
            if letter1 not in word:
                turns=turns+1
            print("Computer's guess = "+letter1+"   "+' '.join(guess) )
            
            if turns==10:
                print("You stumped the computer!")
                break
            
            if word==guess:
                print("The computer guessed your word.")
                turns=100
                break

elif choose=='1':
    words=[]
    w=open("google-10000-english-usa.txt")
    for x in w:
        words.append(x)

    newword=random.choice(words) #randomly select word
    l=len(newword) #count the number of letters
    

    word=[] #creating a list of letters in newword
    for x in range(0,l-1):
        abc=newword[x]
        word.append(abc)
    
    letter1=input("number of spaces = "+str(l-1)+". After seven wrong guesses, you lose. First guess? ") #first letter guess
    
    if letter1==word:
        print("The word is "+''.join(word)+". You won!")
        turns=100

    while letter1 not in a:
        letter1=input("Invalid input. Please guess a lowercase letter.") 
    
    guess=[]
    turns=0
    num=0
 
    while num<1:
        for x in range(0,l-1):
            if letter1==word[x]:
                guess.append(letter1)
            else:
               guess.append('_')
        if letter1 not in word:
            turns=turns+1
        num=num+2

    while turns<7 and num>0:
        while letter1 not in a:
            print("Invalid input. Please guess a lowercase letter.") 
        
        letter1=input(' '.join(guess)+" Number of wrong guesses = "+str(turns)+". Next guess?")
        
        if letter1==''.join(word):
            print("The word is "+''.join(word)+". You won!")
            turns=100
            break
        
        for x in range(0,l-1):
            if letter1==word[x]:
               guess[x]=letter1
            elif guess[x] not in a:
                guess[x]='_'
        
        if letter1 not in word:
            turns=turns+1
        
        
        if turns==7:
            print("The word was "+''.join(word)+". Game over.")
        
        if word==guess:
            print("The word is "+''.join(word)+". You won!")
            turns=100

elif choose=='3':
    newword=input("Player 1, input your word. ")
    l=len(newword) #count the number of letters
    

    word=[] #creating a list of letters in newword
    for x in range(0,l-1):
        abc=newword[x]
        word.append(abc)
    
    letter1=input("number of spaces = "+str(l-1)+". After seven wrong guesses, you lose. Player 2, first guess? ") #first letter guess
    
    if letter1==word:
        print("The word is "+''.join(word)+". You won!")
        turns=100

    while letter1 not in a:
        letter1=input("Invalid input. Please guess a lowercase letter.") 
    
    guess=[]
    turns=0
    num=0
 
    while num<1:
        for x in range(0,l-1):
            if letter1==word[x]:
                guess.append(letter1)
            else:
               guess.append('_')
        if letter1 not in word:
            turns=turns+1
        num=num+2

    while turns<7 and num>0:
        while letter1 not in a:
            print("Invalid input. Please guess a lowercase letter.") 
        
        letter1=input(' '.join(guess)+" Number of wrong guesses = "+str(turns)+". Next guess?")
        
        if letter1==''.join(word):
            print("The word is "+''.join(word)+". You won!")
            turns=100
            break
        
        for x in range(0,l-1):
            if letter1==word[x]:
               guess[x]=letter1
            elif guess[x] not in a:
                guess[x]='_'
        
        if letter1 not in word:
            turns=turns+1
        
        
        if turns==7:
            print("The word was "+''.join(word)+". Game over.")
        
        if word==guess:
            print("The word is "+''.join(word)+". You won!")
            turns=100
    
else:
    print("Invalid input. Start over.")


    
