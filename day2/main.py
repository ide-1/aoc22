with open("input.txt") as file:
    input = file.read()
    input = input.splitlines()

input1 = []

for i in input:
    i = i.split(" ")
    tup = (i[0], i[1])
    input1.append(tup)

print(input1)

score = 0
# part 1
for g in input1:
    if (g[0] == 'A') and (g[1] == 'X'):
        score = score + 1+3  # draw + 1 for rock
    elif (g[0] == 'A') and (g[1] == 'Y'):
        score = score + 2+6
    elif (g[0] == 'A') and (g[1] == 'Z'):
        score = score + 3 + 0
    elif (g[0] == 'B') and (g[1] == 'X'):
        score = score + 1 + 0
    elif (g[0] == 'B') and (g[1] == 'Y'):
        score = score + 2 + 3
    elif (g[0] == 'B') and (g[1] == 'Z'):
        score = score + 3 + 6
    elif (g[0] == 'C') and (g[1] == 'X'):
        score = score + 1 + 6
    elif (g[0] == 'C') and (g[1] == 'Y'):
        score = score + 2 + 0
    elif (g[0] == 'C') and (g[1] == 'Z'):
        score = score + 3 + 3

print(score)
score = 0
# part 2
for g in input1:
    if (g[0] == 'A') and (g[1] == 'X'):
        score = score + 3 + 0
    elif (g[0] == 'A') and (g[1] == 'Y'):
        score = score + 1 + 3
    elif (g[0] == 'A') and (g[1] == 'Z'):
        score = score + 2 + 6
    elif (g[0] == 'B') and (g[1] == 'X'):
        score = score + 1 + 0
    elif (g[0] == 'B') and (g[1] == 'Y'):
        score = score + 2 + 3
    elif (g[0] == 'B') and (g[1] == 'Z'):
        score = score + 3 + 6
    elif (g[0] == 'C') and (g[1] == 'X'):
        score = score + 2 + 0
    elif (g[0] == 'C') and (g[1] == 'Y'):
        score = score + 3 + 3
    elif (g[0] == 'C') and (g[1] == 'Z'):
        score = score + 1 + 6

print(score)
