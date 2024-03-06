import random

puzzle = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', ' '],
]

result = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', ' '],
]


def print_puzzle(puzzle__):
    print("--------------------------------------------------")
    for i in puzzle__:
        print(f'{i}\n')
    print("--------------------------------------------------")


def find_empty(arr):
    for i in range(3):
        for j in range(3):
            if arr[i][j] == " ":
                return i, j


def shuffle(puzzle_, count: int):
    for k in range(count * 100):
        e_row, e_col = find_empty(puzzle_)
        path = random.choice(['up', 'down', 'left', 'right'])

        if path == 'up':
            if e_row < 2:
                puzzle_[e_row][e_col], puzzle_[e_row + 1][e_col] = puzzle_[e_row + 1][e_col], puzzle_[e_row][e_col]

        if path == 'down':
            if e_row > 0:
                puzzle_[e_row][e_col], puzzle_[e_row - 1][e_col] = puzzle_[e_row - 1][e_col], puzzle_[e_row][e_col]

        if path == 'left':
            if e_col < 2:
                puzzle_[e_row][e_col], puzzle_[e_row][e_col + 1] = puzzle_[e_row][e_col + 1], puzzle_[e_row][e_col]

        if path == 'right':
            if e_col > 0:
                puzzle_[e_row][e_col], puzzle_[e_row][e_col - 1] = puzzle_[e_row][e_col - 1], puzzle_[e_row][e_col]


inp = int(input("please enter puzzle level (1, 2, 3): "))

shuffle(puzzle, inp)

print_puzzle(puzzle)

while True:
    if puzzle == result:
        print("you solved the puzzle!!!")
        break

    move = input("enter direction: ")

    if move == "left":
        row, col = find_empty(puzzle)

        if col < 2:
            puzzle[row][col], puzzle[row][col + 1] = puzzle[row][col + 1], puzzle[row][col]

            print_puzzle(puzzle)
            continue
        else:
            print("this move is invalid")
            continue

    if move == "right":
        row, col = find_empty(puzzle)

        if col > 0:
            puzzle[row][col], puzzle[row][col - 1] = puzzle[row][col - 1], puzzle[row][col]

            print_puzzle(puzzle)
            continue
        else:
            print("this move is invalid")
            continue

    if move == "up":
        row, col = find_empty(puzzle)

        if row < 2:
            puzzle[row + 1][col], puzzle[row][col] = puzzle[row][col], puzzle[row + 1][col]

            print_puzzle(puzzle)
            continue

        else:
            print("this move is invalid")
            continue

    if move == "down":
        row, col = find_empty(puzzle)

        if row > 0:
            puzzle[row - 1][col], puzzle[row][col] = puzzle[row][col], puzzle[row - 1][col]

            print_puzzle(puzzle)
            continue
        else:
            print("this move is invalid")
            continue

    if move == "exit":
        break
