from itertools import permutations
from random import random
import numpy as np


def inverse(permutation: list or tuple) -> tuple:
    inv_p = [0] * len(permutation)
    for ii, pp in enumerate(permutation):
        inv_p[pp] = ii
    return tuple(inv_p)


def shorten(permutation: list or tuple, new_length: int) -> tuple:
    """takes a permutation and finds it's corresponding permutation of a shorter length"""
    if len(permutation) < new_length:
        raise ValueError(f"You can't shorten the permutation of length {len(permutation)} to {new_length}")
    new_length = int(new_length)
    new_permutation = np.array(permutation[-new_length:]) - len(permutation) + new_length
    return tuple(new_permutation)


def chunk(permutation_length: int, list_to_chunk: list) -> list:
    """takes a list that's too long for a permutation to scramble and
    chunks it into a size the permutation can handle"""
    per_bin = len(list_to_chunk)/permutation_length
    if per_bin <= 1:
        raise ValueError(f"You can't chunk list of length {len(list_to_chunk)} into {permutation_length} parts")
    new_list = [None] * permutation_length
    remainder = round((per_bin - int(per_bin)) * permutation_length)
    per_bin = int(per_bin)
    last_amount = 0
    for ii in range(permutation_length):
        if remainder > 1:
            remainder -= 1
            extra = 1
        else:
            extra = 0
        new_list[ii] = list_to_chunk[last_amount:(last_amount+per_bin+extra)]
        last_amount += per_bin+extra
    return new_list


class Generate:
    def __init__(self, length: int):
        self.length = length
        self.permutations = list(permutations(range(length)))

    def find_inv_ind(self, perm_num: int):
        perm_to_pair = self.permutations[perm_num]
        inv_perm_num = inverse(perm_to_pair)
        return self.permutations.index(inv_perm_num)

    def get(self, per_num: int) -> tuple:
        return self.permutations[per_num]

    def scramble(self, perm_num: int, list_to_scramble: list):
        perm_num = int(perm_num)
        perm = self.permutations[perm_num]

        if len(list_to_scramble) < self.length:
            perm = shorten(perm, len(list_to_scramble))
        elif len(list_to_scramble) > self.length:
            list_to_scramble = chunk(self.length, list_to_scramble)

        scrambled_list = [0] * len(list_to_scramble)
        for ii, jj in enumerate(perm):
            scrambled_list[ii] = list_to_scramble[jj]
        return scrambled_list

    def unscramble(self, perm_num: int, list_to_unscramble: list):
        perm_num = int(perm_num)
        inv_num = self.find_inv_ind(perm_num)
        unscrambled_list = self.scramble(inv_num, list_to_unscramble)
        return unscrambled_list

    def random(self):
        return int(random() * len(self.permutations))


if __name__ == "__main__":
    list1 = ['The', 'blue', 'pittie']
    list2 = list(range(8, 16))
    list3 = list(range(20))
    print(chunk(8, list3))
    p8 = Generate(8)
    s1 = p8.scramble(3, list1)
    s2 = p8.scramble(3, list2)
    s3 = p8.scramble(3, list3)
    print(s1)
    print(s2)
    print(s3)
    print(p8.unscramble(3, s1))
    print(p8.unscramble(3, s2))
    print(p8.unscramble(3, s3))
