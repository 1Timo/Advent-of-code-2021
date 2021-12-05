def procedure_3(num, num_2, enlarge_1, enlarge_2):
    expand = [num]
    new = 0
    while expand[-1] != num_2:
        helping = expand[new].split()
        changing_ind = len(helping[0][:helping[0].find(',')])
        changing_ind_2 = changing_ind + 1
        first = f'{int(helping[0][:changing_ind]) + (1 if enlarge_1 else -1)}'
        second = f'{int(helping[0][changing_ind_2:]) + (1 if enlarge_2 else -1)}'
        full = first + ',' + second
        expand.append(full)
        new += 1

    return expand


def procedure_2(num, num_2, ind, ind_2, enlarge):
    expand = [num]
    for new in range(abs(int(num[ind:]) - int(num_2[ind_2:])) - 1):
        helping = expand[new].split()
        changing_ind = len(helping[0][:helping[0].find(',')]) + 1
        expand.append(f'{helping[0][:ind]}{str(int(helping[0][changing_ind:]) + (1 if enlarge else -1))}')

    expand.append(num_2)
    return expand


def procedure(num, num_2, ind, ind_2, enlarge):
    expand = [num]
    for new in range(abs(int(num[:ind]) - int(num_2[:ind_2])) - 1):
        helping = expand[new].split()
        changing_ind = len(helping[0][:helping[0].find(',')])
        expand.append(f'{str(int(helping[0][:changing_ind]) + (1 if enlarge else -1))}{helping[0][changing_ind:]}')

    expand.append(num_2)
    return expand


coordinates = []
with open('Bingo.txt') as file:
    for line in file:
        line = line.strip().split(' -> ')
        comma_1 = line[0].find(',')
        comma_2 = line[1].find(',')
        index_1 = len(line[0][:comma_1])
        index_2 = len(line[1][:line[1].find(',')])
        if line[0][:comma_1] != line[1][:comma_2] and\
                line[0][comma_1+1:] != line[1][comma_2+1:]:
            coordinates.append(procedure_3(line[0], line[1],
                                           int(line[0][:index_1]) < int(line[1][:index_2]),
                                           int(line[0][index_1 + 1:]) + 1 < int(line[1][index_2 + 1:])))
            continue

        if line[0][:index_1] == line[1][:index_2]:
            index_1 += 1
            index_2 += 1
            coordinates.append(procedure_2(line[0], line[1],
                                           index_2, index_1, int(line[0][index_1:]) < int(line[1][index_2:])))
            continue

        coordinates.append(procedure(line[0], line[1],
                                     index_1, index_2, int(line[0][:index_1]) < int(line[1][:index_2])))

result = 0
items = {}
for line in coordinates:
    for value in line:
        items[value] = items.get(value, 0) + 1

for item in items.values():
    if item > 1:
        result += 1
