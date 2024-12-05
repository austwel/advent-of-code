import sys
from pathlib import Path
from aocd import data
from numpy import transpose

data = data.strip().split('\n')
h = len(data)
w = len(data[0])
d_list = []
for string in data:
    d_list.append(list(string))
data_transposed = transpose(d_list)
d_t = []
for d in data_transposed:
    string = ''
    for char in d:
        string += char
    d_t.append(string)
data_d1 = []
for i in range(h):
    string = ""
    for j in range(h-i):
        string += data[i+j][j]
    data_d1.append(string)
for i in range(1, w):
    string = ""
    for j in range(w-i):
        string += data[j][i+j]
    data_d1.append(string)

data_d2 = []
for i in range(h):
    string = ""
    for j in range(i+1):
        string += data[i-j][j]
    data_d2.append(string)
for i in range(1, w):
    string = ""
    for j in range(w-i):
        string += data[h-j-1][i+j]
    data_d2.append(string)

def part1():
    sum = 0
    for s in data:
        sum += s.count('XMAS')
        sum += s.count('SAMX')
    for s in d_t:
        sum += s.count('XMAS')
        sum += s.count('SAMX')
    for s in data_d1:
        sum += s.count('XMAS')
        sum += s.count('SAMX')
    for s in data_d2:
        sum += s.count('XMAS')
        sum += s.count('SAMX')
    return sum

def part2():
    sum = 0
    for line in range(1, len(data)-1):
        for char in range(1, len(data[line])-1):
            if data[line][char] == 'A':
                if (data[line-1][char-1] == 'M' and data[line+1][char+1] == 'S') or (data[line-1][char-1] == 'S' and data[line+1][char+1] == 'M'):
                    if (data[line-1][char+1] == 'M' and data[line+1][char-1] == 'S') or (data[line-1][char+1] == 'S' and data[line+1][char-1] == 'M'):
                        sum += 1
    return sum

if __name__ == "__main__":
    print(f' -- Advent of Code: Day {Path(__file__).stem} --')
    if len(sys.argv) < 2 or sys.argv[1] == '1':
        print(f' -> Part 1: {part1()}')
    if len(sys.argv) < 2 or sys.argv[1] == '2':
        print(f' -> Part 2: {part2()}')
