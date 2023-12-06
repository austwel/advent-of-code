import sys

#Parse Puzzle input
def parse(puzzle_input: str) -> any:
    data = puzzle_input.split('\n')
    seed_data = data[0].replace('seeds: ', '').split(' ')
    
    seeds = [int(seed) for seed in seed_data]
    
    seed_ranges = [(int(seed_data[i]), int(seed_data[i+1])) for i in range(0, len(seed_data), 2)]
    
    idxs: list[int] = [
        data.index('seed-to-soil map:'),
        data.index('soil-to-fertilizer map:'),
        data.index('fertilizer-to-water map:'),
        data.index('water-to-light map:'),
        data.index('light-to-temperature map:'),
        data.index('temperature-to-humidity map:'),
        data.index('humidity-to-location map:'),
        len(data)+1
    ]

    m: dict[int, tuple[int, int, int]] = {}
    for map_idx in range(len(idxs)-1):
        for i in range(idxs[map_idx]+1, idxs[map_idx+1]-1):
            if map_idx in m.keys():
                m[map_idx].append(tuple(int(i) for i in data[i].split(' ')))
            else:
                m[map_idx] = [tuple(int(i) for i in data[i].split(' '))]
                
    return seeds, seed_ranges, m

#Solve Part 1
def part1(seeds: list[int], m: dict[int, tuple[int, int, int]]) -> int:
    locs: list[int] = []
    for seed in seeds:
        curr, next = seed, None
        for ranges in m.values():
            for dest, source, l in ranges:
                if source <= curr < source+l:
                    next = dest+curr-source
                    break
            if next is None: next = curr
            curr, next = next, None
        
        locs.append(curr)
    return min(locs)
            
#Solve Part 2
def part2(seed_ranges: list[tuple[int, int]], map: dict[int, tuple[int, int, int]]) -> int:
    lowest_possible_loc = None
    loc = 0
    while not lowest_possible_loc:
        loc+=1
        curr, next = loc, None
        for ranges in reversed(list(map.values())):
            for dest, source, l in ranges:
                if dest <= curr < dest+l:
                    next = source+curr-dest
                    break
            if next is None: next = curr
            curr, next = next, None
        
        for init, l in seed_ranges:
            if init <= curr < init+l:
                lowest_possible_loc = loc
        
    return lowest_possible_loc

#Solve Both Parts
def solve(puzzle_input: str) -> tuple[int, int]:
    seeds, seed_ranges, m = parse(puzzle_input)
    solution1 = part1(seeds, m)
    solution2 = part2(seed_ranges, m)
    return solution1, solution2

#Boilerplate
if __name__ == "__main__":
    f = open('test.txt' if len(sys.argv) > 1 and sys.argv[1] == 'test' else 'input.txt', 'r')
    puzzle_input = f.read().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))