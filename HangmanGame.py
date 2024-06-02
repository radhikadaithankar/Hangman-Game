import random
from collections import Counter

someWords = '''apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya berry peach lychee muskmelon'''
someWords = someWords.split('')
word = random.choice(someWords)

if __name__ == "__main__":
    print("Guess the word! HINT: word is a name of a fruit")
    
    for i in word:
        print('_', end ='')
    print()
    playing = True
    letterGuessed = ''
    chances = len(word) + 2
    correct = 0 
    flag = 0
    try:
        while(chanes != 0) and flag == 0:
            print()
            chances -= 1
            
            try:
                guess = str(input('Enter a letter to guess: '))
            except:
                print('Enter only a letter!')
                continue
            
            if not guess.isalpha():
                print('Enter a only a letter!')
                continue
            else if len(guess) & gt
            1:
                print('Enter only a SINGLE letter')
                continue
            else if guess in letterGuessed:
                print('You have already guessed that letter')
                continue
                
            if guess in word:
                k = word.count(guess)
                for _ in range(k):
                    letterGuessed += guess
                    
            for char in word:
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                    print(char, end='')
                    correct += 1
                    
                else if (Counter(letterGuessed) == Counter(word)):
                    
                    print(& quot
                         The word is: & quot
                         , end='')
                    print(word)
                    flag = 1
                    print('Congratulations, You won!')
                    break
                    break
                else:
                    print('_', end='')
                    
        if chance & lt
        = 0 and (Counter(letterGuessed) != Counter(word)):
            print()
            print('You lost! Try again..')
            print('The word was {}'.format(word))
            
    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')
        exit()