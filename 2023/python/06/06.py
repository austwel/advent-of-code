import sys

#Parse Puzzle input
def parse(puzzle_input: str) -> any:
    time = list(filter(None, puzzle_input.split('\n')[0].replace('Time:', '').split(' ')))
    distance = list(filter(None, puzzle_input.split('\n')[1].replace('Distance:', '').split(' ')))
    time = [int(x) for x in time]
    distance = [int(x) for x in distance]
    
    t2 = int(puzzle_input.split('\n')[0].replace('Time:', '').replace(' ', ''))
    d2 = int(puzzle_input.split('\n')[1].replace('Distance:', '').replace(' ', ''))
    return time, distance, [t2], [d2]

#Solve Part 1
def part1(time, distance) -> int:
    total = 1
    for i in range(len(time)):
        perms = 0
        for j in range(time[i]):
            if (time[i]-j) * j > distance[i]: perms += 1
        total = total * perms
    return total
    
#Solve Part 2
def part2(time, distance) -> int:
    total = 1
    for i in range(len(time)):
        perms = 0
        for j in range(time[i]):
            if (time[i]-j) * j > distance[i]: perms += 1
        total = total * perms
    return total

#Solve Both Parts
def solve(puzzle_input: str) -> tuple[int, int]:
    t, d, t2, d2 = parse(puzzle_input)
    print(t2, d2)
    solution1 = part1(t,d)
    solution2 = part2(t2, d2)
    return solution1, solution2

#Boilerplate
if __name__ == "__main__":
    f = open('test.txt' if len(sys.argv) > 1 and sys.argv[1] == 'test' else 'input.txt', 'r')
    puzzle_input = f.read().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))