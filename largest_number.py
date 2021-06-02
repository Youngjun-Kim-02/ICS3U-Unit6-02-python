#!/usr/bin/env python3

# Created by: Youngjun Kim
# Created on: Dec 2019
# This program uses a list as a parameter

import random


def find_largest_number(random_numbers):

    Largest_number = random_numbers[0]

    for counter in range (0, len(random_numbers)):
        if Largest_number < random_numbers[counter]:
            Largest_number = random_numbers[counter]

    return Largest_number


def main():
    # this function uses a list

    random_numbers = []

    # input
    for loop_counter in range(1, 11):
        a_number = random.randint(1,100)
        random_numbers.append(a_number)
        print("The random number {0} is: {1} ".format(loop_counter, a_number))
    print("")

    # call the function
    Largest_number = find_largest_number(random_numbers)

    # output
    print("The largest number is: {0} ".format(Largest_number))


if __name__ == "__main__":
    main()
