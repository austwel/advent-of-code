import sys
from enum import IntEnum
from typing import Self
from collections import Counter
from functools import cached_property

class HandType(IntEnum):
    HIGHCARD = 0
    PAIR = 1
    TWOPAIR = 2
    THREEOFAKIND = 3
    FULLHOUSE = 4
    FOUROFAKIND = 5
    FIVEOFAKIND = 6
    
class Hand(object):
    def __init__(self, line: str, with_joker: bool):
        self._with_joker = with_joker
        self._string: str = line.split(' ')[0]
        self._bid: int = int(line.split(' ')[1])
        self._hand_type = None
    
    @property
    def hand_type(self) -> HandType:
        if self._hand_type is None: self._hand_type = self.calculate_hand_type()
        return self._hand_type
        
    def calculate_hand_type(self) -> HandType:
        d = dict(sorted(Counter(self._string).items(), key=lambda k: k[1], reverse=True))
        if self._with_joker and 'J' in list(d):
            if len(list(d)) == 1: return HandType.FIVEOFAKIND
            d[list(d)[1 if list(d)[0] == 'J' else 0]] += d.pop('J')
        if d[list(d)[0]] == 5: return HandType.FIVEOFAKIND
        if d[list(d)[0]] == 4: return HandType.FOUROFAKIND
        if d[list(d)[0]] == 3 and len(list(d)) > 1 and d[list(d)[1]] == 2: return HandType.FULLHOUSE
        if d[list(d)[0]] == 3: return HandType.THREEOFAKIND
        if d[list(d)[0]] == 2 and len(list(d)) > 1 and d[list(d)[1]] == 2: return HandType.TWOPAIR
        if d[list(d)[0]] == 2: return HandType.PAIR
        return HandType.HIGHCARD
        
    @property
    def bid(self) -> int:
        return self._bid
    
    def __str__(self) -> str:
        return self._string
        
    def __getitem__(self, idx):
        item = self._string[idx]
        if item == 'A': return 14
        elif item == 'K': return 13
        elif item == 'Q': return 12
        elif item == 'J': return 1 if self._with_joker else 11
        elif item == 'T': return 10
        else: return int(item)
        
    def __lt__(self, hand: Self) -> bool:
        if self.hand_type < hand.hand_type: return True
        if self.hand_type > hand.hand_type: return False
        for i in range(5):
            if self[i] < hand[i]:
                return True
            if self[i] > hand[i]:
                return False
            
    def __eq__(self, hand: Self) -> bool:
        self.hand_type is hand.hand_type and str(self) == str(hand)
        
    def __gt__(self, hand: Self) -> bool:
        if self.hand_type > hand.hand_type: return True
        if self.hand_type < hand.hand_type: return False
        for i in range(5):
            if self[i] > hand[i]:
                return True
            if self[i] < hand[i]:
                return False
          
#Parse Input
def parse(puzzle_input: str) -> any:
    return puzzle_input
    
#Solve Part 1
def part1(data: str) -> int:
    hands = sorted([Hand(line, False) for line in data.split('\n')])
    return sum((i+1) * hands[i].bid for i in range(len(hands)))

#Solve Part 2
def part2(data: str) -> int:
    hands = sorted([Hand(line, True) for line in data.split('\n')])
    return sum((i+1) * hands[i].bid for i in range(len(hands)))

#Solve Both Parts
def solve(puzzle_input: str) -> tuple[int, int]:
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

#Boilerplate
if __name__ == "__main__":
    f = open('test.txt' if len(sys.argv) > 1 and sys.argv[1] == 'test' else 'input.txt', 'r')
    puzzle_input = f.read().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))