import sys
from math import prod

#Parse Puzzle input
def parse(s: str):
    return {int(l.split(': ')[0][5:]): [{b.split(' ')[1]: int(b.split(' ')[0]) for b in g.split(', ')} for g in l.split(': ')[1].split('; ')] for l in s.split('\n')}

def part1(s: str):
    return sum(int(l.split(': ')[0][5:]) for l in s.split('\n') if not any(g for g in l.split(': ')[1].split('; ') if any(b for b in g.split(', ') if int(b.split(' ')[0])>{'red':12,'blue':14,'green':13}[b.split(' ')[1]])))

def part2(s: str):
    return sum(prod(max(int(g[g.index(c)-3:g.index(c)]) for g in l.split(':')[1].split(';') if c in g) for c in ['red','blue','green']) for l in s.split('\n'))

#Solve Both Parts
def solve(puzzle_input) -> tuple[int, int]:
    solution1 = part1(puzzle_input)
    solution2 = part2(puzzle_input)
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