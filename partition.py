from collections.abc import Sequence
from itertools import filterfalse, tee
from typing import Callable, Tuple, TypeVar

T = TypeVar('T')


# Given an input sequence and a predicate, return two lists, one where the elements
# of the sequence are false for the predicate and one where they are true, e.g.
# partition(range(10), pred=is_odd) -> [0, 2, 4, 6, 8], [1, 3, 5, 7, 9]
# Taken from the partition recipe found in the itertools documentation:
# https://docs.python.org/3/library/itertools.html#itertools-recipes
def partition(seq: Sequence[T], pred: Callable[[T], bool]) -> Tuple[Sequence[T], Sequence[T]]:
    seq1, seq2 = tee(seq)
    return list(filterfalse(pred, seq1)), list(filter(pred, seq2))
