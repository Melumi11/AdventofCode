# https://adventofcode.com/2021/day/1
data = []
with open("day1/input.txt") as file:
    for line in file:
        data.append(int(line.rstrip()))
out = 0
i = 0
while i < (len(data) - 3):
    if data[i+3] - data[i] > 0: out += 1
    i += 1
print(out)
