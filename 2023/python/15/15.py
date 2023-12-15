import sys

#Parse Puzzle input
def parse(puzzle_input: str) -> any:
    return puzzle_input.split(',')

#Solve Part 1
def part1(data: any) -> int:
    total = 0
    for code in data:
        total += hasher(code)
    return total
    
#Solve Part 2
def part2(data: list[str]) -> int:
    total = 0
    hashmap: dict[int, list[tuple[str, int]]] = dict()
    for code in data:
        if code[-1].isnumeric():
            hsh = hasher(code[:-2])
            if hsh in hashmap.keys():
                broken = False
                for i in range(len(hashmap[hsh])):
                    if hashmap[hsh][i][0] == code[:-2]:
                        hashmap[hsh][i] = ((code[:-2], int(code[-1])))
                        broken = True
                        break
                if not broken: hashmap[hsh].append((code[:-2], int(code[-1])))
            else:
                hashmap[hsh] = [(code[:-2], int(code[-1]))]
        else:
            hsh = hasher(code[:-1])
            if hsh in hashmap.keys():
                for t in hashmap[hsh]:
                    if t[0] == code[:-1]:
                        hashmap[hsh].remove(t)
                        if hashmap[hsh] == []:
                            hashmap.pop(hsh)
        
    for key, value in hashmap.items():
        for i in range(len(value)):
            total += (key+1) * (i+1) * (value[i][1])
        
    return total

def hasher(string: str) -> int:
    total = 0
    for char in string:
        total = ((total + ord(char))*17) % 256
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