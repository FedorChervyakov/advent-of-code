import heapq

def main(filename):
    print(f'Scanning file {filename}')

    # top n elves
    n = 3
    # first is max
    best_elves = [(0, 0) for _ in range(n)]

    current_sum = 0
    current_elf = 1

    def update_best_elves(line):
        nonlocal current_sum, current_elf, best_elves
        line = line.strip()

        if len(line) == 0:
            for i in range(n):
                if current_sum > best_elves[i][0]:
                    best_elves.insert(i, (current_sum, current_elf))
                    break

            best_elves = best_elves[:3]

            current_sum = 0
            current_elf += 1
        else:
            current_sum += int(line)

    with open(filename, 'r') as f:
        for line in f:
            update_best_elves(line)

        update_best_elves('')

    total = 0

    for ix, (max_calories, best_elf) in enumerate(best_elves):
        total += max_calories
        print(f'Elf {best_elf} is the {ix+1}. They carry {max_calories}!')

    print(f'In total best elves carry {total} calories')



if __name__ == '__main__':
    main('test_input.txt')

    from pathlib import Path
    path = Path('input.txt')
    if path.exists():
        main('input.txt')
