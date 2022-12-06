def main(filename):
    print(f'Reading strategy from {filename}')

    # columns are our moves
    # rows are opponent moves
    # indexing goes as rock paper scissors
    maap = [
        [3, 6, 0],
        [0, 3, 6],
        [6, 0, 3],
    ]

    trans = dict(
        zip(
            ['A', 'B', 'C', 'X', 'Y', 'Z'],
            [1, 2, 3, 1, 2, 3],
        )
    )

    total_score = 0

    with open(filename, 'r') as f:
        for line in f:
            opponent, me = line.strip().split()

            # fight score. we subtract one to get the index in maap
            round_score = maap[trans[opponent]-1][trans[me]-1]

            # item score
            round_score += trans[me]

            total_score += round_score

    print(f'Total score is {total_score}')


if __name__ == '__main__':
    main('test_input.txt')

    from pathlib import Path
    path = Path('input.txt')
    if path.exists():
        main('input.txt')
