#  given an array, find the integer that appears an odd number of times.

#  there will always be only one integer that appears an od number of times.


def find_it(seq):
    freq_dict = {}

    for num in seq:
        if num not in freq_dict:
            freq_dict[num] = 1
        else:
            freq_dict[num] += 1

    for k, v in freq_dict.items():
        if v % 2 != 0:
            return k


# Planning:  given an array
# freq_dict
# for each N
# store its count
# loop through array
# for each number add n += 1
# loop through key_values in freq_dict
# if key_values % 2 = 0
# return 1
