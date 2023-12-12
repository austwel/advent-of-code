import sys

#Parse Puzzle input
def parse(puzzle_input: str) -> any:
    return puzzle_input.split('\n')

#Solve Part 1
def part1(data: list[str]) -> int:
    expac_rows: list[int] = []
    expac_cols: list[int] = []
    dimensions = (len(data), len(data[0]))
    i = 0
    while i < dimensions[1]:
        if all(True if d == '.' else False for d in [data[n][i] for n in range(dimensions[0])]):
            expac_cols.append(i)
        i += 1
    i=0
    while i < dimensions[0]:
        if all(True if d == '.' else False for d in data[i]):
            expac_rows.append(i)
        i += 1
    locs = []
    i = 0
    while i < dimensions[0]:
        j = 0
        while j < dimensions[1]:
            if data[i][j] == '#':
                locs.append((i, j))
            j+=1
        i+=1
    
    total = 0
    i = 0
    while i < len(locs)-1:
        j = i+1
        while j < len(locs):
            total += calculate_distance(locs[i], locs[j], expac_rows, expac_cols, 2)
            j+=1
        i+=1
        
    return total
        
        
def calculate_distance(loc1: tuple[int, int], loc2: tuple[int, int], er: list[int], ec: list[int], value: int):
    deltax = abs(loc1[1]-loc2[1])
    deltay = abs(loc1[0]-loc2[0])
    for expac_row in er:
        if loc1[0] > expac_row and loc2[0] < expac_row or loc1[0] < expac_row and loc2[0] > expac_row:
            deltay += value-1
    for expac_col in ec:
        if loc1[1] > expac_col and loc2[1] < expac_col or loc1[1] < expac_col and loc2[1] > expac_col:
            deltax += value-1
    return deltax + deltay
    
#Solve Part 2
def part2(data: any) -> int:
    expac_rows: list[int] = []
    expac_cols: list[int] = []
    dimensions = (len(data), len(data[0]))
    i = 0
    while i < dimensions[1]:
        if all(True if d == '.' else False for d in [data[n][i] for n in range(dimensions[0])]):
            expac_cols.append(i)
        i += 1
    i=0
    while i < dimensions[0]:
        if all(True if d == '.' else False for d in data[i]):
            expac_rows.append(i)
        i += 1
    locs = []
    i = 0
    while i < dimensions[0]:
        j = 0
        while j < dimensions[1]:
            if data[i][j] == '#':
                locs.append((i, j))
            j+=1
        i+=1
    
    total = 0
    i = 0
    while i < len(locs)-1:
        j = i+1
        while j < len(locs):
            total += calculate_distance(locs[i], locs[j], expac_rows, expac_cols, 1000000)
            j+=1
        i+=1
        
    return total

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