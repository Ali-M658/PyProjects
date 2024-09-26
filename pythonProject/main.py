import random

def minion_game(play1inp, countp1, enteredsets):
    if not any(vowel in play1inp for vowel in 'aeiou '):
        return f'Vowels only, {name1}.', countp1

    if play1inp in enteredsets:
        return f'{name1}, you have already entered this.', countp1

    enteredsets.add(play1inp)
    flea = randword.count(play1inp)
    for _ in range(flea):
        countp1 += 1

    if countp1 >= 10:
        return f'The score for {name1} is over 10. {name1} wins!', countp1

    return f'{name1}, your set of letters appeared {flea} times. You have {countp1} points.', countp1

def minion_game2(play2inp, countp2, enteredsets):
    if not any(consonant in 'bcdfghjklmnpqrstvwxyz ' for consonant in play2inp):
        return f'Consonants only, {name2}.', countp2

    if play2inp in enteredsets:
        return f'{name2}, you have already entered this.', countp2

    enteredsets.add(play2inp)
    fly = randword.count(play2inp)
    for l in range(fly):
        countp2 += 1

    if countp2 >= 10:
        return f'The score for {name2} is over 10. {name2} wins!', countp2

    return f'{name2}, your set of letters appeared {fly} times. You have {countp2} points.', countp2

words = 'elephant,mountain,sunshine,notebook,rainbow,journey,paradise,treasure,festival,harmony'
randword = random.choice(words.split(','))

name1 = input('What is your name, player 1? ')
name2 = input('What is your name, player 2? ')
print(f'Hello, {name1} and {name2}. The word is: {randword}')
countp1 = 0
countp2 = 0

# Consonant and vowel set
enteredsets = set()
discardelements = ['a', 'e', 'i', 'o', 'u']
discardelementsc = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
consonantset = set(randword)
vowelset = set(randword)

for elements in discardelements:
    consonantset.discard(elements)

for elemente in discardelementsc:
    vowelset.discard(elemente)

while True:
    play1inp = input(f'Enter vowels only and the more occurrences in {randword}, the more points: ')
    result1, countp1 = minion_game(play1inp, countp1, enteredsets)
    print(result1)

    play2inp = input(f'Enter consonants only and the more occurrences in {randword}, the more points: ')
    result2, countp2 = minion_game2(play2inp, countp2, enteredsets)
    print(result2)

    if len(enteredsets) == len(randword):
        playagain2 = input('All have been entered. Play again? (y/n) ')
        if playagain2 == 'y':
            countp1 = 0
            countp2 = 0
            enteredsets.clear()
            continue
        elif playagain2 == 'n':
            break
        else:
            continue

    if len(vowelset) == len(enteredsets.difference(consonantset)):
        playagain2 = input('All vowels have been entered. Play again? (y/n) ')
        if playagain2 == 'y':
            countp1 = 0
            countp2 = 0
            enteredsets.clear()
            continue
        elif playagain2 == 'n':
            break
        else:
            continue

    if len(consonantset) == len(enteredsets.difference(vowelset)):
        playagain2 = input('All consonants have been entered. Play again? (y/n) ')
        if playagain2 == 'y':
            countp1 = 0
            countp2 = 0
            enteredsets.clear()
            continue
        elif playagain2 == 'n':
            break
        else:
            continue

    if countp1 >= 10 or countp2 >= 10:
        playagain = input('It\'s a Tie! Play again? (y/n) ')
        if playagain == 'y':
            countp1 = 0
            countp2 = 0
            enteredsets.clear()
            continue
        elif playagain == 'n':
            break
        else:
            continue

