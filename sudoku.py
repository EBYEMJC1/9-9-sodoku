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


fill()

for rows in rows_columns:
    print(" ".join(str(x) for x in rows))
