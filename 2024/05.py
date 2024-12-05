import sys
from pathlib import Path
from aocd import data

a, b = data.split('\n\n')
rules = {}
for rule in a.split('\n'):
    prv, nxt = rule.split('|')
    if nxt in rules.keys():
        rules[nxt].append(prv)
    else:
        rules[nxt] = [prv]

updates = [pages.split(',') for pages in b.split('\n')]

def part1():
    sum = 0
    for update in updates:
        value = update[(len(update)-1)//2]
        broken = False
        for i in range(len(update)):
            if not update[i] in rules.keys(): rules[update[i]] = []
            for prv in rules[update[i]]:
                if prv in update[i::]:
                    broken = True
                    break
            if broken: break
        if not broken:
            sum += int(value)
    return sum

def part2():
    sum = 0
    for update in updates:
        broken = False
        i = 0
        while i < len(update):
            if not update[i] in rules.keys(): continue
            for prv in rules[update[i]]:
                if prv in update[i::]:
                    broken = True
                    i2 = update.index(prv)
                    update[i], update[i2] = update[i2], update[i]
                    i-=1
                    break
            i+=1
        value = int(update[(len(update)-1)//2])
        if broken: sum += value
    return sum

if __name__ == "__main__":
    print(f' -- Advent of Code: Day {Path(__file__).stem} --')
    if len(sys.argv) < 2 or sys.argv[1] == '1':
        print(f' -> Part 1: {part1()}')
    if len(sys.argv) < 2 or sys.argv[1] == '2':
        print(f' -> Part 2: {part2()}')
