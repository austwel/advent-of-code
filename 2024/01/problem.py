import os
import sys

def funct(filepath):
    list1 = []
    list2 = []
    with open(filepath, 'r') as file:
        for line in file:
            entries = line.strip().split('   ')
            list1.append(entries[0])
            list2.append(entries[1])
    return list1, list2

def part1(filepath):
    list1, list2 = funct(filepath)
    list1.sort()
    list2.sort()
    sum = 0
    for i in range(len(list1)):
        sum += abs(int(list1[i])-int(list2[i]))
    return sum

def part2(filepath):
    list1, list2 = funct(filepath)
    list1.sort()
    list2.sort()
    sum = 0
    dt = {}
    for i in range(len(list2)):
        if list2[i] in dt.keys():
            dt[list2[i]]=dt[list2[i]]+1
        else:
            dt[list2[i]]=1
    for i in range(len(list1)):
        if list1[i] in dt.keys():
            sum += dt[list1[i]]*int(list1[i])
    return sum

if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == '1':
        print(f'Part 1: {part1(sys.argv[1])}')
    elif len(sys.argv) > 2 and sys.argv[2] == '2':
        print(f'Part 2: {part2(sys.argv[1])}')
    else:
        print(f'Part 1: {part1(sys.argv[1])}')
        print(f'Part 2: {part2(sys.argv[1])}')
