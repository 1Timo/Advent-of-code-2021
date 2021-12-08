import itertools


def kokot(values):
    # si si myslel, ze ma odrbes co ?
    try:
        return digit_template.index("".join(sorted(values)))

    except ValueError:
        return None


def check(segments):
    return kokot(segments) is not None


def uz_mam_nervy_jak_kokot_funkcia(value, arrangement):
    return ''.join(arrangement[val] for val in value)


def finding_codes(file):
    array = []
    with open(file) as file:
        file = [value.split(' | ') for value in file.read().split('\n')[:-1]]
        for signal, outputs in file:
            signal = signal.split()
            outputs = outputs.split()
            for arrangementes in permutation:
                arrangement = [uz_mam_nervy_jak_kokot_funkcia(value, arrangementes) for value in signal]
                if all(check(values) for values in arrangement):
                    outputs = [uz_mam_nervy_jak_kokot_funkcia(output, arrangementes) for output in outputs]
                    outputs = [kokot(output) for output in outputs]
                    array.append(outputs)
                    break
    return array


template = 'abcdefg'
digit_template = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
result = 0

"""
Making every possible arrangement
"""
permutation = itertools.permutations(template)

"""
Making every possible arrangement for every possible arragement :D
"""
permutation = [{key: value for key, value in zip(template, arrangement)} for arrangement in permutation]
result = sum([int("".join(map(str, results))) for results in finding_codes('Bingo.txt')])
