def main(filename):
    print(f'Reading assignments from {filename}')

    res = 0

    with open(filename, 'r') as f:
        for line in f:
            elf1, elf2 = [tuple(map(int, x.split('-'))) for x in line.strip().split(',')]

            if elf1[0] == elf2[0]:
                res += 1
            elif elf1[0] < elf2[0]:
                res += int(elf2[1] <= elf1[1])
            else:
                res += int(elf1[1] <= elf2[1])

    print(f'Total number of contained ranges is {res}')


if __name__ == '__main__':
    main('test_input.txt')

    from pathlib import Path
    path = Path('input.txt')
    if path.exists():
        main('input.txt')
