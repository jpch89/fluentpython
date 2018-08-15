# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   2018/8/15 20:53

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])
# 也可以用字符串隔开字段
# Card = collections.namedtuple('Card', 'rank suit')

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
    
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]


beer_card = Card('7', 'diamonds')
print(beer_card)
# Card(rank='7', suit='diamonds')

deck = FrenchDeck()
print(len(deck))
# 52

print(deck[0])

print(deck[-1])

from random import choice
print(choice(deck))

print(choice(deck))

print(choice(deck))


