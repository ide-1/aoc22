with open("input.txt") as file:
    input = file.read()
    input = input.splitlines()

weight = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
          'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

score = 0

for i in input:
    l = int(len(i)/2)
    scorestart = score
    for a in range(l):
        print('a = ', i[a])
        if score > scorestart:
            break
        for b in range(l, len(i)):
            print("b = ", i[b])
            if i[a] == i[b]:
                print("they're the same and the weight is: ",
                      (weight.index(i[a])+1))
                score = score + weight.index(i[a]) + 1
                break


print(score)

score = 0

for i in range(0, len(input), 3):
    scorestart = score
    for j in input[i]:
        if score > scorestart:
            break
        for k in input[i+1]:
            if score > scorestart:
                break
            for l in input[i+2]:
                if j == k == l:
                    print(j)
                    score = score + weight.index(j) + 1
                    break
print(score)
