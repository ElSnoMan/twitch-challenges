from typing import List

a1 = ['a', 'b', 'c']
a2 = ['b', 'c', 'd']

b1 = ['c', 'a', 'b', 'c']
b2 = ['b', 'c', 'd']


def print_dupes(list_a, list_b):
    dupes = []
    for item in list_a:
        if item in list_b:
            dupes.append(item)
    return set(dupes)


strings = ["abc", "def", "abc", "ghi"]
s = "abc"


def print_duplicate_count(list_s: List[str], string):
    if list_s:
        return list_s.count(string)


if __name__ == '__main__':
    # print(print_dupes(a1, a2))
    # print(print_dupes(b1, b2))
    print(print_duplicate_count(strings, s))
