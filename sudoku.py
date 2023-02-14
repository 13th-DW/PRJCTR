'''
Determine if a 9 x 9 Sudoku board is valid.
Only the filled cells need to be validated according to the following rules:

- Each row must contain the digits 1-9 without repetition.
- Each column must contain the digits 1-9 without repetition.
- Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗
║ 8 │ 5 │   ║   │   │ 2 ║ 4 │   │   ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║ 7 │ 2 │   ║   │   │   ║   │   │ 9 ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║   │   │ 4 ║   │   │   ║   │   │   ║
╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣
║   │   │   ║ 1 │   │ 7 ║   │   │ 2 ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║ 3 │   │ 5 ║   │   │   ║ 9 │   │   ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║   │ 4 │   ║   │   │   ║   │   │   ║
╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣
║   │   │   ║   │ 8 │   ║   │ 7 │   ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║   │ 1 │ 7 ║   │   │   ║   │   │   ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║   │   │   ║   │ 3 │ 6 ║   │ 4 │   ║
╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝

'''

sudoku = [
    ['8', '5', ' ', ' ', ' ', '2', '4', ' ', ' '],  # len == 9
    ['7', '2', ' ', ' ', ' ', ' ', ' ', ' ', '9'],
    [' ', ' ', '4', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', '1', ' ', '7', ' ', ' ', '2'],
    ['3', ' ', '5', ' ', ' ', ' ', '9', ' ', ' '],
    [' ', '4', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', '8', ' ', ' ', '7', ' '],
    [' ', '1', '7', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', '3', '6', ' ', '4', ' ']
]  # len == 9


def is_sudoku_row_valid(sudoku: list) -> bool:

    for i in sudoku:
        a = set()
        for j in i:
            if j.isdigit():
                if j not in a:
                    a.add(j)
                else:
                    return False
    return True


def is_sudoku_col_valid(sudoku: list) -> bool:

    # for columns
    for col in range(9):
        a = set()

        # for elements
        for elem in range(9):
            if sudoku[elem][col].isdigit():
                if sudoku[elem][col] not in a:
                    a.add(sudoku[elem][col])
                else:
                    return False

    return True


def is_sudoku_part_valid(sudoku: list) -> bool:

    for row in range(0, 9, 3):
        for part in range(0, 9, 3):
            a = set()
            for i in range(row, 3+row):
                for j in range(part, 3+part):
                    if sudoku[i][j].isdigit():
                        if sudoku[i][j] not in a:
                            a.add(sudoku[i][j])
                        else:
                            return False

    return True


def is_sudoku_valid(sudoku: list) -> bool:
    return is_sudoku_row_valid(sudoku) == is_sudoku_col_valid(sudoku) == is_sudoku_part_valid(sudoku) == True


