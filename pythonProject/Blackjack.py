import random as rd
hit_or_stand_player2 = input('Press enter to start: ')


Aces = ["Ace of Hearts", "Ace of Spades", "Ace of Diamonds", "Ace of Clubs"]
Twos = ["2 of Hearts", "2 of Spades", "2 of Diamonds", "2 of Clubs"]
Threes = ["3 of Hearts", "3 of Spades", "3 of Diamonds", "3 of Clubs"]
Fours = ["4 of Hearts", "4 of Spades", "4 of Diamonds", "4 of Clubs"]
Fives = ["5 of Hearts", "5 of Spades", "5 of Diamonds", "5 of Clubs"]
Sixes = ["6 of Hearts", "6 of Spades", "6 of Diamonds", "6 of Clubs"]
Sevens = ["7 of Hearts", "7 of Spades", "7 of Diamonds", "7 of Clubs"]
Eights = ["8 of Hearts", "8 of Spades", "8 of Diamonds", "8 of Clubs"]
Nines = ["9 of Hearts", "9 of Spades", "9 of Diamonds", "9 of Clubs"]
Tens = ["10 of Hearts", "10 of Spades", "10 of Diamonds", "10 of Clubs"]
Jacks = ["Jack of Hearts", "Jack of Spades", "Jack of Diamonds", "Jack of Clubs"]
Queens = ["Queen of Hearts", "Queen of Spades", "Queen of Diamonds", "Queen of Clubs"]
Kings = ["King of Hearts", "King of Spades", "King of Diamonds", "King of Clubs"]

def get_randomcard(a):
    if a == 1:
        return rd.choice(Aces)
    elif a == 2:
        return rd.choice(Twos)
    elif a == 3:
        return rd.choice(Threes)
    elif a == 4:
        return rd.choice(Fours)
    elif a == 5:
        return rd.choice(Fives)
    elif a == 6:
        return rd.choice(Sixes)
    elif a == 7:
        return rd.choice(Sevens)
    elif a == 8:
        return rd.choice(Eights)
    elif a == 9:
        return rd.choice(Nines)
    elif a == 10:
        return rd.choice(Tens)
    elif a == 11:
        return rd.choice(Jacks)
    elif a == 12:
        return rd.choice(Queens)
    elif a == 13:
        return rd.choice(Kings)
def get_randomcards(b):
    if b == 1:
        return rd.choice(Aces)
    elif b == 2:
        return rd.choice(Twos)
    elif b == 3:
        return rd.choice(Threes)
    elif b == 4:
        return rd.choice(Fours)
    elif b == 5:
        return rd.choice(Fives)
    elif b == 6:
        return rd.choice(Sixes)
    elif b == 7:
        return rd.choice(Sevens)
    elif b == 8:
        return rd.choice(Eights)
    elif b == 9:
        return rd.choice(Nines)
    elif b == 10:
        return rd.choice(Tens)
    elif b == 11:
        return rd.choice(Jacks)
    elif b == 12:
        return rd.choice(Queens)
    elif b == 13:
        return rd.choice(Kings)

total = 0

total_player_2 = 0

a = int(rd.randint(1,13))
b = int(rd.randint(1,13))
def blackjack(a,q ,total, hit_or_stand):
    if hit_or_stand.lower() == 'hit':
        a = int(rd.randint(1,13))
        total += a+q
        print(f'Player 1 got the {get_randomcard(a)}. Your total is now:{total}')

    elif hit_or_stand.lower() == 'stand':
        print('Your total is still the same.')


    return int(total), int(q)
def blackjack2(b ,v , total_player_2, hit_or_stand_player2):

    if hit_or_stand_player2.lower() == 'hit':
        b = int(rd.randint(1,13))
        total_player_2 += b+v
        print(f'Player 2 got the {get_randomcards(b)}. Your total is now:{total_player_2}')

    elif hit_or_stand_player2.lower() == 'stand':
        print('Your total is still the same.')

    return int(total_player_2), int(v)
q = 0

v = 0
while True\
        :
    hit_or_stand = input('Hit or Stand? ')
    total, q = blackjack(a, q, total, hit_or_stand)
    if total >= 21:
        print('Player 1 exceeded the amount. Player 2 wins!')
        break
    hit_or_stand_player2 = input('Player 2, Hit or Stand? ')
    total_player_2, v = blackjack2(b,v, total_player_2, hit_or_stand_player2)
    if total_player_2 > 21:
        print('Player 2 exceeded the amount. Player 1 wins!')
        break
