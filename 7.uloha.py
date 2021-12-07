def function(file: str, start: bool):
    with open(file) as file:
        file = tuple(map(int, file.read().split(',')))

    highest = max(file)
    lowest = 0
    for line in range(0, highest):
        outcome = 0
        for value in file:
            outcome += sum([value for value in range(abs(value - line) + 1)]) if start else abs(value - line)

        if lowest > outcome or not lowest:
            lowest = outcome

        else:
            break

    return lowest


result = function('Bingo.txt', True)

if __name__ == '__main__':
    print()
