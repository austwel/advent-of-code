import sys
import math

#Parse Puzzle input
def parse(puzzle_input: str) -> any:
    return puzzle_input.split('\n')

#Solve Part 1
def part1(data: any) -> int:
    total = 0
    for card in data:
        card_winners = 0
        numbers = card.split(':')[1]
        winners = numbers.split('|')[0].split(' ')
        mine = numbers.split('|')[1].split(' ')
        winners = list(filter(None, winners))
        mine = list(filter(None, mine))
        for m in mine:
            if m in winners:
                card_winners+=1
        if card_winners > 0:
            total += math.pow(2, card_winners-1)
        
    return total
    
#Solve Part 2
def part2(data: any) -> int:
    scratchcards = 0
    to_play = []
    for _ in data: to_play.append(1)
    for c in range(len(to_play)):
        print(to_play)
        scratchcards += to_play[c]
        card_winners = 0
        winners = list(filter(None, data[c].split(':')[1].split('|')[0].split(' ')))
        mine = list(filter(None, data[c].split(':')[1].split('|')[1].split(' ')))
        print(winners, mine)
        for m in mine:
            if m in winners:
                card_winners+=1
        print(card_winners)
        for i in range(card_winners):
            print(to_play[c+1+i], to_play[c+1+i] + to_play[c])
            to_play[c+1+i] = to_play[c+1+i] + to_play[c]
    
    return scratchcards
                
#Solve Both Parts
def solve(puzzle_input: str) -> tuple[int, int]:
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

#Boilerplate
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        f = open('test.txt', 'r')
        puzzle_input = f.read().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
    else:
        f = open('input.txt', 'r')
        puzzle_input = f.read().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))