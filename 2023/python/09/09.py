import sys

#Parse Puzzle input
def parse(puzzle_input: str) -> any:
    return [[int(x) for x in line.split(' ')] for line in puzzle_input.split('\n')]

def part1(data: list[str]) -> int:
    return sum(next_number(nums) for nums in data)

def part2(data: list) -> int:
    return sum(prev_number(nums) for nums in data)

def next_number(lst) -> int:
    return 0 if all(x == 0 for x in lst) else lst[-1] + next_number([lst[i+1] - lst[i] for i in range(len(lst)-1)])
    
def prev_number(lst) -> int:
    return 0 if all(x == 0 for x in lst) else lst[0] - prev_number([lst[i+1] - lst[i] for i in range(len(lst)-1)])
    
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