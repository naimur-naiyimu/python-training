import random
meaningful_word=['dog','cow','cat']

def geneate_letters(meaningful_word):
    word=random.choice(meaningful_word)
    letters=list(word)
    random.shuffle(letters)
    return letters

point=0
wrong=0
while True:
    letters=geneate_letters(meaningful_word)
    for letter in letters:
        print(letter,end=' ')
    word=input('\nenter a meaningfull word:')
    if word in meaningful_word:
        point += 1
        print(f'correct ! your point is {point}')
    else:
        wrong+=1
        point=('not match')
    if wrong ==3:
        print(f'game is over ! your point is {point}')
        d=input('do you want continue?if yes enter y')
        if d.upper()=='Y':
            point=0
            wrong=0
            continue
        else:
            break
            
         
    
