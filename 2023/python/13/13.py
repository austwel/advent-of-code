import sys

#Parse Puzzle input
def parse(puzzle_input: str) -> any:
    data: list[list[str]] = []
    count = 0
    rows = puzzle_input.split('\n')
    for row in rows:
        if row != '':
            if count == len(data):
                data.append([row])
            else:
                data[count].append(row)
        else:
            count += 1
    return data

#Solve Part 2
def part2(data: any) -> int:
    total = 0
    for im in data:
        h = h_image2(im)*100
        if h > 0: 
            total += h
            print(h)
        else:
            im = [''.join(i) for i in zip(*im)]
            h = h_image2(im)
            if h == 0:
                print('No line found for')
                print("\n".join(im))
            print(h)
            total += h
        
    return total

def h_image2(image: list[str]) -> int:
    cache = [image[0]]
    i = 1
    while i < len(image):
        j = 0
        temp_cache = cache.copy()
        differences = 0
        while len(temp_cache) > 0:
            if i+j == len(image):
                if differences == 1: return i
                else: break
            if image[i+j] != temp_cache[0]:
                differences += sum([1 for idx in range(len(temp_cache[0])) if image[i+j][idx] != temp_cache[0][idx]])
            if differences > 1:
                break
            temp_cache.pop(0)
            j += 1
        if len(temp_cache) == 0 and differences == 1:
            return i
        else:
            cache.insert(0, image[i])
        i+=1
    return 0

def h_image(image: list[str]) -> int:
    cache = [image[0]]
    i = 1
    while i < len(image):
        j = 0
        temp_cache = cache.copy()
        while len(temp_cache) > 0:
            if i+j == len(image):
                return i
            if image[i+j] != temp_cache[0]: 
                break
            temp_cache.pop(0)
            j += 1
        if len(temp_cache) == 0:
            return i
        else:
            cache.insert(0, image[i])
        i+=1
    return 0
    
#Solve Part 1
def part1(data: any) -> int:
    total = 0
    for im in data:
        h = h_image(im)*100
        if h > 0: 
            total += h
        else:
            im = [''.join(i) for i in zip(*im)]
            h = h_image(im)
            if h == 0:
                print('No line found for')
                print("\n".join(im))
            total += h
        
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