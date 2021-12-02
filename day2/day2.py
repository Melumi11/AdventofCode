# https://adventofcode.com/2021/day/2
x = 0
y = 0
with open("day2/input.txt") as file:
    for line in file:
        text = line.rstrip()
        if text.startswith("f"): x += int(text[-1])
        if text.startswith("u"): y -= int(text[-1])
        if text.startswith("d"): y += int(text[-1])
print(x*y)