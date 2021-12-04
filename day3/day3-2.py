# https://adventofcode.com/2021/day/3
data = []
binlen = 12 # length of input line
digits = [0] * binlen
o2 = [0] * binlen
co2 = [0] * binlen
usabledigits = 0
with open("day3/input.txt") as file:
    for line in file:
        data.append(line.rstrip())

def process(index): # to get rid of the lines we don't need
    if usabledigits == 1:
        i = 0
        while i < binlen:
            o2[i] = int(stored[i])
            i += 1
        return
    if digits[index] >= usabledigits/2: 
        o2[index] = 1
        digits[index] = 1
    else: digits[index] = 0
    i = 0
    while i < len(data):
        if int(data[i][index]) != digits[index]:
            data[i] = [-1] * binlen
        i += 1

ind = 0
while ind < binlen: # goes through every digit
    usabledigits = 0
    for i in data: # goes through every line
        if i[ind-1] != -1:
            usabledigits += 1
            digits[ind] += int(str(i)[ind])
            if usabledigits == 1: stored = i
    process(ind)
    ind += 1

data = [] # repeat for co2
digits = [0] * binlen
usabledigits = 0
with open("day3/input.txt") as file:
    for line in file:
        data.append(line.rstrip())

def process(index):
    if usabledigits == 1:
        i = 0
        while i < binlen:
            co2[i] = int(stored[i])
            i += 1
        return
    if digits[index] < usabledigits/2: 
        co2[index] = 1
        digits[index] = 1
    else: digits[index] = 0
    i = 0
    while i < len(data):
        if int(data[i][index]) != digits[index]:
            data[i] = [-1] * binlen
        i += 1

ind = 0
while ind < binlen:
    usabledigits = 0
    for i in data:
        if i[ind-1] != -1:
            usabledigits += 1
            digits[ind] += int(str(i)[ind]) # use to find average
            if usabledigits == 1: stored = i
    process(ind)
    ind += 1

i = 0
o2int = 0
co2int = 0
while i < binlen:
    o2int += o2[i] * 2**(binlen-1-i)
    co2int += co2[i] * 2**(binlen-1-i)
    i += 1
print(o2int*co2int)
print(o2)
print(co2)
"""
    find the first digit of digits
    find second digits by sorting through first digits first
    etc.
"""