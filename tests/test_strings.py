from typing import Tuple


def word_count(string) -> Tuple[str, str]:
    words = string.split()
    longest = max(words, key=len)
    shortest = min(words, key=len)
    return longest, shortest


def test_shortest_and_longest():
    sentence = 'a cow jumped over the moon'
    longest, shortest = word_count(sentence)
    assert longest == 'jumped'
    assert shortest == 'a'
