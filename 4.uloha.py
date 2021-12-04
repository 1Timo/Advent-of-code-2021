def control(win=True):
    for number, column in enumerate(table):
        if not win and number in checking:
            continue

        for i in range(height):
            variables = ([], [])
            for index in range(height):
                if column[index + i * height] in chosen:
                    variables[0].append(True)
                if column[index * height + i] in chosen:
                    variables[1].append(True)

                if len(variables[0]) == 5:
                    if win:
                        return True, number

                    else:
                        yield number

                elif len(variables[1]) == 5:
                    if win:
                        return True, number

                    else:
                        yield number

    return False


with open('Bingo.txt') as file:
    file = file.read().split('\n\n')

selecting = file[0].split(',')
height = file[1].count('\n') + 1
# does not need width because if height does not equal width, the problem is in file, not in program :)

table = [line.split() for line in file[1:]]
chosen = tuple([value for value in selecting[:4]])


''' # If you want to win ->

result = 0
for selected in selecting[4:]:
    chosen += selected,
    check = control()
    if isinstance(check, tuple):
        for value in table[check[1]]:
            if value not in chosen:
                result += int(value)

        break

win = result * int(chosen[-1])
'''

# If you want to lose ->
checking = set()
last = 0
result = 0
for selected in selecting[4:]:
    chosen += selected,
    won = list(control(False))
    if won:
        last = int(won[-1])
        [checking.add(value) for value in won]
        if len(checking) == len(table):
            for value in table[last]:
                if value not in chosen:
                    result += int(value)
            break

lose = result * int(chosen[-1])
