with open("input.txt") as file:
    input = file.read()
    input = input.splitlines()

input1 = []

for i in input:
    input1.append(i.split(","))

input2 = []

for i in input1:
    input3 = []
    for j in i:
        input3.append(list(map(int, j.split("-"))))
    input2.append(input3)
print(input2)

score = 0

for [elf1, elf2] in input2:
    if ((elf1[0] <= elf2[0] and elf1[1] >= elf2[1]) or (elf2[0] <= elf1[0] and elf2[1] >= elf1[1])):
        score += 1
print(score)

score2 = 0

for [elf1, elf2] in input2:
    if ((elf1[0] <= elf2[1] and elf1[1] >= elf2[0])
            or (elf2[0] <= elf1[1] and elf2[1] >= elf1[0])):
        score2 += 1

print(score2)
