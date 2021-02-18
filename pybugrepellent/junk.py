line = "Hello"

list = []

for i in range(len(line)):
    list.append(line[i])
print(list)

list2 = [char for char in line]
print(list2)
