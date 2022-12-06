with open("input.txt") as file:
    input = file.read()
    input = input.splitlines()


stacks = {
    "1": ['T', 'Q', 'V', 'C', 'D', 'S', 'N'],
    "2": ['V', 'F', 'M'],
    "3": ['M', 'H', 'N', 'P', 'D', 'W', 'Q', 'F'],
    "4": ['F', 'T', 'R', 'Q', 'D'],
    "5": ['B', 'V', 'H', 'Q', 'N', 'M', 'F', 'R'],
    "6": ['Q', 'W', 'P', 'N', 'G', 'F', 'C'],
    "7": ['T', 'C', 'L', 'R', 'F', 'W'],
    "8": ['S', 'N', 'Z', 'T'],
    "9": ['N', 'H', 'Q', 'R', 'J', 'D', 'S', 'M']
}

for i in range(10):
    input.pop(0)

# print(input)
input1 = []

for i in input:
    i = i.split(" ")
    i.pop(4)
    i.pop(2)
    i.pop(0)
    input1.append(i)

print(input1)

# for task in input1:
#     for crates in range(int(task[0])):
#         crate = stacks[task[1]].pop(0)
#         stacks[task[2]].insert(0, crate)
#
#
# answer = ""
# for stack in stacks.values():
#     answer += stack[0]
#
# print(answer)

for task in input1:
    for crates in range(int(task[0])-1, -1, -1):
        print(task[0], crates)
        crate = stacks[task[1]].pop(crates)
        stacks[task[2]].insert(0, crate)

answer = ""
for stack in stacks.values():
    answer += stack[0]

print(answer)
