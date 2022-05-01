# https://adventofcode.com/2021/day/1

f = open("day1/input.txt", "r")
out = -1
prev = -1
for x in f:
    if (int(x) > prev): out += 1
    prev = int(x)
print(out)

f.close()
# f.read(#ofchars)
# f.readline()