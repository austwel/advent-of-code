import sys
import time
start_time = time.time()

#Parse Puzzle input
def parse(puzzle_input: str) -> any:
    map = puzzle_input.split('\n')
    for i in range(len(map)):
        if 'S' in map[i]:
            start_pos = (i, map[i].index('S'))
            map[i] = map[i].replace('S', get_start(start_pos, map))
    return map, start_pos

def get_start(pos, map):
    above = map[pos[0]-1][pos[1]] in '|F7'
    left = map[pos[0]][pos[1]-1] in '-J7'
    down = map[pos[0]+1][pos[1]] in '|JL'
    right = map[pos[0]][pos[1]+1] in '-FL'
    return 'F' if right and down \
        else 'J' if left and above \
        else 'L' if right and above \
        else '7' if left and down \
        else '|' if above and down \
        else '-'
    
#Solve Part 1
def part1(map: list[str], start: tuple[int, int]) -> int:
    c, pos, move = 0, start, None
    while True:
        pos, move = go_next(map, pos, move)
        c+=1
        if pos == start: 
            return int(c/2)
        
#Solve Part 2
def part2(map: list[str], start: tuple[int, int]) -> int:
    pos, locs, move = start, {}, None
    locs[pos[0]] = [False] * len(map[0])
    locs[pos[0]][pos[1]] = True
    while True:
        pos, move = go_next(map, pos, move)
        if pos[0] in locs.keys():
            locs[pos[0]][pos[1]] = True
        else:
            locs[pos[0]] = [False] * len(map[0])
            locs[pos[0]][pos[1]] = True
        if pos == start: return calculate_inside(map, locs)

def calculate_inside(map, locs) -> int:
    total = 0
    for line in range(len(map)):
        if line not in locs.keys(): continue
        count=False
        for tile in range(len(map[0])):
            if locs[line][tile]:
                if map[line][tile] in '|F7':
                    count = not count
            elif count:
                total += 1
    return total
        
def go_next(map, pos, last):
    if map[pos[0]][pos[1]] in '|LJ' and last != 'down': return (pos[0]-1, pos[1]), 'above'
    if map[pos[0]][pos[1]] in '-7J' and last != 'right': return (pos[0], pos[1]-1), 'left'
    if map[pos[0]][pos[1]] in '|7F' and last != 'above': return (pos[0]+1, pos[1]), 'down'
    if map[pos[0]][pos[1]] in '-LF' and last != 'left': return (pos[0], pos[1]+1), 'right'

#Solve Both Parts
def solve(puzzle_input: str) -> tuple[int, int]:
    map, start = parse(puzzle_input)
    print('Parse time: ' + str(time.time() - start_time))
    solution1 = part1(map, start)
    print('P1 time: ' + str(time.time() - start_time))
    solution2 = part2(map, start)
    print('P2 time: ' + str(time.time() - start_time))
    return solution1, solution2

#Boilerplate
if __name__ == "__main__":
    f = open('test.txt' if len(sys.argv) > 1 and sys.argv[1] == 'test' else 'input.txt', 'r')
    puzzle_input = f.read().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))