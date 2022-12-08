from string import ascii_letters

def main(filename):
    print(f'Reading items from {filename}')

    prio = dict(zip(ascii_letters, range(1, 53)))

    total_score = 0

    with open(filename, 'r') as f:
        i = 0
        common_items = set()
        for line in f:
            line = line.strip()

            items = set(line)

            if i == 0:
                common_items = items
            else:
                common_items.intersection_update(items)

            if i == 2:
                common_item = common_items.pop()
                total_score += prio[common_item]
                i = 0
            else:
                i += 1

    print(f'Total score is {total_score}')


if __name__ == '__main__':
    main('test_input.txt')

    from pathlib import Path
    path = Path('input.txt')
    if path.exists():
        main('input.txt')
