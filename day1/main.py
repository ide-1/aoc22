
with open("input.txt") as file:
    input = file.read()
    input = input.splitlines()
# print(input)
max = 0
elf = 0
for i in input:

    if i == "":
        if elf > max:
            max = elf
        elf = 0

    else:
        elf += int(i)

print(max)

elf = 0

one = 0
two = 0
three = 0

for i in input:

    if i == "":
        if elf > one:
            three = two
            two = one
            one = elf
        elif elf > two: 
            three = two
            two = elf
        elif elf > three:
            three = elf

        elf = 0

    else:
        elf += int(i)

print(one+two+three)
