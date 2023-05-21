import math
from math import sqrt
import random


while True:
    try:
        number_of_rows_columns = int(input("Enter a perfect square as the size of your board: "))
        sqrt = math.sqrt(int(number_of_rows_columns))
        is_it_perfect_square = int(sqrt + .5) ** 2
        if int(number_of_rows_columns) != int(is_it_perfect_square):
            raise ValueError(f"{int(number_of_rows_columns)} is not a perfect square")
        break
    except ValueError:
        print("Invalid input please input a perfec square")

rows_columns = [[0]*number_of_rows_columns for i in range(number_of_rows_columns)]

def generate_random_number():
    return random.randint(1, number_of_rows_columns)

for row in range(number_of_rows_columns):
    for column in range(number_of_rows_columns):
        rand_num = generate_random_number()
        print(rand_num)