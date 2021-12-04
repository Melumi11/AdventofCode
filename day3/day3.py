# https://adventofcode.com/2021/day/3
data = []
binlen = 12 # length of input line length
digits = [0] * binlen
gamma = [0] * binlen
epsilon = [0] * binlen
with open("day3/input.txt") as file:
    for line in file:
        data.append(line.rstrip())
for i in data:
    j = 0
    while j < binlen:
        digits[j] += int(i[j])
        j += 1
i = 0
while i < binlen:
    if digits[i] > len(data)/2: gamma[i] = 1
    else: epsilon[i] = 1
    i += 1
i = 0
gammaint = 0
epsilonint = 0
while i < binlen:
    gammaint += gamma[i] * 2**(binlen-1-i)
    epsilonint += epsilon[i] * 2**(binlen-1-i)
    i += 1
print(gammaint*epsilonint)