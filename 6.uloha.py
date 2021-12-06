from collections import Counter


def day_6(file: str, lowest: int, highest: int, reproduction_day: int, days_to_count: int) -> int:
    initial = Counter(list(map(int, open(file).read().split(','))))
    value_holder = {key: (0 if key not in initial else initial[key]) for key in range(lowest, highest + 2)}

    for _ in range(days_to_count):
        for key in sorted(value_holder):
            if not key:
                value_holder[highest + 1] = value_holder[key]

            elif key and key != highest + 1:
                value_holder[key - 1] = value_holder[key]

            else:
                value_holder[highest] = value_holder[key]
                value_holder[reproduction_day] = value_holder.get(reproduction_day) + value_holder[key]
                value_holder[key] = 0

    return sum(value_holder.values())


result = day_6('Bingo.txt', 0, 8, 6, 256)
if __name__ == '__main__':
    pass
