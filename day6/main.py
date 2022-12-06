with open("input.txt") as file:
    input = file.read()

set = set()
for i in range(len(input)):
    for j in range(4):
        set.add(input[i+j])
    if len(set) == 4:
        print(i+4)
        break
    set.clear()
set.clear()
for i in range(len(input)):
    for j in range(14):
        set.add(input[i+j])
    if len(set) == 14:
        print(i+14)
        break
    set.clear()
