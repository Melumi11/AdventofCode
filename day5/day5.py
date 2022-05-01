# https://adventofcode.com/2021/day/5
numbers = []
data = []
with open("day5/input.txt") as file:
    numbers = [int(s) for s in file.readline().split(',')]
    for line in file:
        data.append(line.rstrip())
    blocks = len(data)/6 # number of boards
boards = [[[], [], [], [], []]] * int(blocks) # array of 2d arrays which stores boards

currentboard = 0
i = 0
while currentboard < blocks: # sets the boards in boards to the boards
    j = 0
    while data[i] != "":
        if data[i][0] == " ": data[i] = data[i][1:]
        boards[currentboard][j] = [int(s) for s in data[i].replace("  ", " ").split(' ')]
        j += 1
        i += 1
    currentboard += 1
    i += 1