from math import prod


def exist(table: list, new_first: int, new_second: int):
    try:
        if table[new_first][new_second] != 9:
            return [new_first, new_second]

        return None

    except IndexError:
        return None


def basin_finder(table: list, first: int, second: int, value: list):
    value.append(exist(table, first + 1, second))
    value.append(exist(table, first - 1, second))
    value.append(exist(table, first, second + 1))
    value.append(exist(table, first, second - 1))
    value = [val for val in value if val is not None if val[0] >= 0 if val[1] >= 0]
    table[first][second] = 9
    result = 0
    for first, second in value:
        result += basin_finder(table, first, second, [])
    return result


def day_9_part_2(table: str):
    table = [list(map(int, line)) for line in table]
    basins = []
    for line in range(len(table)):
        for value in range(len(table[line])):
            if table[line][value] is None or table[line][value] == 9:
                continue
            before_count = len([None for line in table for value in line if value == 9])
            basin_finder(table, line, value, [])
            after_count = len([None for line in table for value in line if value == 9])
            basins.append(after_count - before_count)
    return prod(sorted(basins, reverse=True)[:3])


def day_9(file: str):
    table = open(file).read().rstrip().split('\n')
    highlits = ()
    for line in range(len(table)):
        for var in range(len(table[line])):
            current = int(table[line][var])
            if not line:
                if not var:
                    if int(table[line + 1][var]) > current and int(table[line][var + 1]) > current:
                        highlits += (current + 1),

                elif var and var != len(table[line]) - 1:
                    if int(table[line + 1][var]) > current and int(table[line][var + 1]) > current \
                            and int(table[line][var - 1]) > current:
                        highlits += (current + 1),
                else:
                    if int(table[line + 1][var]) > current and int(table[line][var - 1]) > current:
                        highlits += (current + 1),

            elif line and line != len(table) - 1:
                if not var:
                    if int(table[line + 1][var]) > current and int(table[line][var + 1]) > current and \
                            int(table[line - 1][var]) > current:
                        highlits += (current + 1),

                elif var and var != len(table[line]) - 1:
                    if int(table[line + 1][var]) > current and int(table[line][var + 1]) > current and \
                            int(table[line - 1][var]) > current and int(table[line][var - 1]) > current:
                        highlits += (current + 1),

                else:
                    if int(table[line + 1][var]) > current and int(table[line][var - 1]) > current and \
                            int(table[line - 1][var]) > current:
                        highlits += (current + 1),

            else:
                if not var:
                    if int(table[line - 1][var]) > current and int(table[line][var + 1]) > current:
                        highlits += (current + 1),

                elif var and var != len(table[line]) - 1:
                    if int(table[line - 1][var]) > current and int(table[line][var + 1]) > current \
                            and int(table[line][var - 1]) > current:
                        highlits += (current + 1),

                else:
                    if int(table[line - 1][var]) > current and int(table[line][var - 1]) > current:
                        highlits += (current + 1),

    print('Task_1:', sum(highlits))
    print('Task_2:', day_9_part_2(table))


if __name__ == '__main__':
    day_9('Bingo.txt')
