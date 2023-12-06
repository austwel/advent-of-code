import sys

#Parse Puzzle input
def parse(puzzle_input: str) -> any:
    return puzzle_input

#Solve Part 1
def part1(data: any) -> int:
    return
    
#Solve Part 2
def part2(data: any) -> int:
    return

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