import sys
from itertools import combinations
from functools import cache

#Parse Puzzle input
def parse(puzzle_input: str) -> any:
    return puzzle_input.split('\n')

#Solve Part 1
def part1(data: list[str]) -> int:
    total = 0
    for row in data:
        count = 0
        problem = ".".join(list(filter(None, row.split(' ')[0].split('.')))) + '.'
        parts = [int(x)+1 for x in row.split(' ')[1].split(',')]
        conc_parts = [sum([parts[j] for j in range(i)]) for i in range(len(parts))]
        last_parts = [len(problem)-sum([parts[j] for j in range(i, len(parts))]) for i in range(len(parts))]
        
        problem_len = len(problem)
        parts_len = len(parts)
        
        cs = list(combinations(range((problem_len+parts_len)), parts_len))
        
        combos = [combo for combo in cs if all([combo[i]>=conc_parts[i] and combo[i]<=last_parts[i] for i in range(parts_len)])]
        
        for combo in combos:
            done = [None] * problem_len
            possible = True
            i = 0
            while i < len(combo):
                for j in range(parts[i]):
                    if done[combo[i]+j]:
                        possible = False
                        break
                    if j == parts[i]-1:
                        if problem[combo[i]+j] == '#':
                            possible = False
                            break
                        else:
                            done[combo[i]+j] = True
                    elif problem[combo[i]+j] in '?#':
                        done[combo[i]+j] = True
                    else:
                        possible = False
                        break
                if not possible:
                    break
                i+=1
                
            i = 0
            while i < problem_len:
                if not done[i] and problem[i] == '#':
                    possible = False
                    break
                i+=1
                
            if possible:
                count += 1
                
        total += count
    return total
    
#Solve Part 2
def part2(data: list[str]) -> int:
    total = 0
    for row in data:
        problem = "?".join([("." if row[0] == "." else "") + ".".join(list(filter(None, row.split(' ')[0].split('.')))) + ("." if row.split(' ')[0][-1] == "." else "")] * 5) + "."
        p = [int(x) for x in row.split(' ')[1].split(',')]
        parts = []
        for _ in range(5):
            parts.extend(p)
        parts = tuple(parts)
        total += cached_counter(problem, parts)
        
    return total

@cache
def cached_counter(problem: str, parts: list[int]) -> int:
    count = 0
    if not parts:
        if '#' in problem: return 0
        else: return 1
    part = parts[0]
    for i in range(len(problem)-len(parts)-sum(parts[1:])-part+1):
        if problem[i+part] == '#': continue
        elif '#' in problem[:i]: break
        elif '.' not in problem[i:i+part]: 
            count += cached_counter(problem[i+part+1:], parts[1:])
    return count

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