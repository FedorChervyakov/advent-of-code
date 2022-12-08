from string import ascii_letters

def main(filename):
    print(f'Reading items from {filename}')

    prio = dict(zip(ascii_letters, range(1, 53)))

    total_score = 0

    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            half_ix = len(line) // 2

            first, second = line[:half_ix], line[half_ix:]

            items_first, items_second = set(first), set(second)

            total_score += prio[items_first.intersection(items_second).pop()]

    print(f'Total score is {total_score}')


if __name__ == '__main__':
    main('test_input.txt')

    from pathlib import Path
    path = Path('input.txt')
    if path.exists():
        main('input.txt')
