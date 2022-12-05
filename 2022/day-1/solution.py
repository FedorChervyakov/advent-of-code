def main(filename):
    print(f'Scanning file {filename}')
    current_elf = 1
    best_elf = 1

    current_sum = 0
    max_calories = 0

    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()

            if len(line) == 0:
                if current_sum > max_calories:
                    best_elf = current_elf
                    max_calories = current_sum

                current_sum = 0
                current_elf += 1
            else:
                current_sum += int(line)

    print(f'Elf {best_elf} is the best. They carry {max_calories}!')



if __name__ == '__main__':
    main('test_input.txt')

    from pathlib import Path
    path = Path('input.txt')
    if path.exists():
        main('input.txt')
