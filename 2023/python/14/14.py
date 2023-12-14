import sys
from functools import cache

#Parse Puzzle input
def parse(puzzle_input: str) -> any:
    data = puzzle_input.split('\n')
    rows = len(data)
    cols = len(data[0])
    static = []
    static2 = []
    static3 = []
    static4 = []
    flexi = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 'O': flexi.append((i, j))
            elif data[i][j] == '#': 
                static.append((i, j))
                static2.append((j, rows-i-1))
                static3.append((rows-i-1, cols-j-1))
                static4.append((cols-j-1, i))
                
    return static, static2, static3, static4, flexi, rows, cols

def get_load(boulder: tuple[int, int], static: list[tuple[int, int]], edge: int) -> tuple[int, tuple[int, int]]:
    row, col = boulder
    inline = set(s for s in static if s[1] == col)
    while row >= 0:
        if (row, col) in inline:
            return (edge - row-1, (row+1, col))
        row -= 1
    return edge, (0, col)

#Solve Part 1
def part1(static: list, flexi: list, edge) -> int:
    total = 0
    st = static.copy()
    flexi.sort(key=lambda x: x[0])
    for boulder in flexi:
        t, new = get_load(boulder, st, edge)
        total += t
        st.append(new)
    return total
    
#Solve Part 2
def part2(static: list, static2: list, static3: list, static4: list, flexi: list, rows, cols) -> int:
    states = dict()
    start = 0
    end = 0
    for cycle_count in range(1, 1000000000):
        flexi = quad_move_spin(static, static2, static3, static4, flexi, rows, cols)
        state = create_state(flexi, rows, cols)
        if state in states.keys():
            print(f'Cycle start: {states[state]}, Cycle end: {cycle_count}')
            start, end = states[state], cycle_count
            break
        else: states[state] = cycle_count
    
    for _ in range((1000000000 - start) % (end-start)):
        flexi = quad_move_spin(static, static2, static3, static4, flexi, rows, cols)
    
    
    total = stay_load(flexi, rows)
    return total

def stay_load(boulders: list, edge: int):
    return sum(edge-x[0] for x in boulders)

def create_state(boulders: list[tuple[int, int]], rows: int, cols: int):
    ret = ''
    boulder_s = set(boulders)
    for i in range(rows):
        for j in range(cols):
            if (i, j) in boulder_s:
                ret += '1'
            else:
                ret += '0'
    return ret

def quad_move_spin(static: list, static2: list, static3: list, static4: list, flexi: list, rows: int, cols: int):
    n_flexi = moveall(flexi, static)
    flexi = spin(n_flexi, rows)
    n_flexi = moveall(flexi, static2)
    flexi = spin(n_flexi, cols)
    n_flexi = moveall(flexi, static3)
    flexi = spin(n_flexi, rows)
    n_flexi = moveall(flexi, static4)
    flexi = spin(n_flexi, cols)
    return flexi

def moveall(boulders: list, static: list):
    boulders.sort(key=lambda x: x[0])
    n_static, n_flexi = static.copy(), []
    for boulder in boulders:
        new = move(boulder, n_static)
        n_static.append(new)
        n_flexi.append(new)
    return n_flexi
            
def move(boulder: tuple[int, int], static: list[tuple[int, int]]) -> tuple[int, tuple[int, int]]:
    row, col = boulder
    inline = [s for s in static if s[1] == col]
    while row >= 0:
        if (row, col) in inline:
            return (row+1, col)
        row -= 1
    return (0, col)

def spin(flexi, rows):
    n_flexi = []
    for b in flexi:
        n_flexi.append((b[1], rows-b[0]-1))
    return n_flexi

#Solve Both Parts
def solve(puzzle_input: str) -> tuple[int, int]:
    static, static2, static3, static4, flexi, rows, cols = parse(puzzle_input)
    solution1 = part1(static, flexi, rows)
    solution2 = part2(static, static2, static3, static4, flexi, rows, cols)
    return solution1, solution2

#Boilerplate
if __name__ == "__main__":
    f = open('test.txt' if len(sys.argv) > 1 and sys.argv[1] == 'test' else 'input.txt', 'r')
    puzzle_input = f.read().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))