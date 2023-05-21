import math
import random

while True:
    try:
        number_of_rows_columns = int(input("Enter a perfect square as the size of your board: "))
        sqrt = math.isqrt(number_of_rows_columns)
        is_it_perfect_square = sqrt ** 2
        if number_of_rows_columns != is_it_perfect_square:
            raise ValueError(f"{number_of_rows_columns} is not a perfect square")
        break
    except ValueError:
        print("Invalid input. Please input a perfect square.")

rows_columns = [[0] * number_of_rows_columns for _ in range(number_of_rows_columns)]


def generate_random_number(valid_choices):
    return random.choice(valid_choices)


def fill():
    for row in range(number_of_rows_columns):
        for column in range(number_of_rows_columns):
            valid_choices = list(range(1, number_of_rows_columns + 1))
            while valid_choices:
                rand_num = generate_random_number(valid_choices)
                valid_choices.remove(rand_num)
                if validate(rand_num, row, column):
                    break
            rows_columns[row][column] = rand_num


def validate(num, row, column):
    for i in range(number_of_rows_columns):
        if rows_columns[row][i] == num and i != column:
            return False
        if rows_columns[i][column] == num and i != row:
            return False
    start_row_index_for_sub_block = (row // sqrt) * sqrt
    start_column_index_for_sub_block = (column // sqrt) * sqrt
    for j in range(sqrt):
        for k in range(sqrt):
            if rows_columns[start_row_index_for_sub_block + j][start_column_index_for_sub_block + k] == num and (start_row_index_for_sub_block + j != row or start_column_index_for_sub_block + k != column):
                return False
    return True


def remove_random_elements(difficulty):
    total_elements = number_of_rows_columns ** 2
    elements_to_remove = int(total_elements * difficulty)
    indices = random.sample(range(total_elements), elements_to_remove)

    for index in indices:
        row = index // number_of_rows_columns
        column = index % number_of_rows_columns
        rows_columns[row][column] = 0


def print_board():
    for rows in rows_columns:
        print(" ".join(str(x) if x != 0 else "_" for x in rows))


def play_sudoku():
    print("Let's play Sudoku!")
    print("Enter row and column indices (starting from 1) followed by the number to fill.")
    print("Enter 'q' to quit.")
    while True:
        user_input = input("Enter your move: ")
        if user_input == "q":
            print("Quitting the game.")
            break
        try:
            row, column, num = map(int, user_input.split())
            if not (1 <= row <= number_of_rows_columns and 1 <= column <= number_of_rows_columns):
                print("Invalid move. Row and column indices are out of range.")
                continue
            if rows_columns[row - 1][column - 1] != 0:
                print("Invalid move. This cell is already filled.")
                continue
            if not validate(num, row - 1, column - 1):
                print("Invalid move. The number conflicts with existing elements.")
                continue
            rows_columns[row - 1][column - 1] = num
            print_board()
            if all(0 not in row for row in rows_columns):
                print("Congratulations! You have solved the Sudoku.")
                break
        except ValueError:
            print("Invalid input. Please enter row and column indices (starting from 1) followed by the number.")

# Set the difficulty level (percentage of elements to remove)
difficulty = 0.5  # Adjust this value to change the difficulty

fill()
remove_random_elements(difficulty)
print_board()
play_sudoku()
