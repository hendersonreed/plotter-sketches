#!/bin/env python3

"""
x range: 0,10300

y range: 0, 7650
"""

from random import randint

x_min = 50
y_min = 50
x_max = 10300 - x_min
y_max = 7650 - y_min
pen = 1


def random_valid_coord():
    return (randint(x_min, x_max-1), randint(y_min, y_max-1))


def random_square():
    (random_x, random_y) = random_valid_coord()
    side_length_y = randint(y_min, y_max - random_y)
    side_length_x = randint(x_min, x_max - random_x)

    scalar = (random_y / (2 * y_max)) + 0.5
    side_length = int(min(side_length_x, side_length_y) * scalar)

    # random pen
    # origin
    print(f"PA{random_x},{random_y};")
    print("PD;")

    # lower left
    print(f"PR0,{side_length};")

    # lower right
    print(f"PR{side_length},0;")

    # upper right
    print(f"PR0,-{side_length};")

    # origin
    print(f"PA{random_x},{random_y};")

    # pu
    print("PU;")


print(f"IN;SP{pen};")
print("PA0,0")
for x in range(1, 60):
    """
    if (x % 20) == 0:
        pen = pen + 1
        print(f"SP{pen};")
        """
    random_square()
print("SP0;")
