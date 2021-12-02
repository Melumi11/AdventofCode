# https://adventofcode.com/2021/day/2#part2
x = 0
aim = 0
y = 0
with open("day2/input.txt") as file:
    for line in file:
        text = line.rstrip()
        if text.startswith("f"): 
            y += aim * int(text[-1])
            x += int(text[-1])
        if text.startswith("u"): aim -= int(text[-1])
        if text.startswith("d"): aim += int(text[-1])
print(x*y)