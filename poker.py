import random
import pandas as pd
import numpy as np

class freshDeck:
    def __init__(self):
        suits = ['Spades','Hearts','Diamonds','Clubs']
        names = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

        cards = []

        for suit in suits:
            for name in names:
                cards.append([name,suit])
        cards = pd.DataFrame(cards,columns={'Name','Suit'})
        self.table = cards

class shuffleDeck:
    def __init__(self,cards):
        shuffled = cards.sample(frac = 1).reset_index()
        shuffled = shuffled.drop(columns='index')
        self.table = shuffled

class dealCards:
    def __init__(self,cards):
        players_cards = []
        for x in range(2):
            drop_indices = np.random.choice(cards.index, 1, replace=False)
            ind = int(drop_indices)
            pick = cards.loc[ind]
            cards = cards.drop([ind],axis=0).reset_index().drop(columns='index')
            players_cards.append([pick['Name'],pick['Suit']])
        players_cards = pd.DataFrame(players_cards,columns={'Name','Suit'})
        print (players_cards)
        self.table = cards


fresh = freshDeck().table
deck = shuffleDeck(fresh).table
player_count = 6
for x in range(player_count):
    deck = dealCards(deck).table
print (deck)