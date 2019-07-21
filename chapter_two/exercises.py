from typing import List, Dict, NamedTuple
from random import shuffle
# performance advantage of binary search over linear search by creating a list of one million numbers and timing how long it takes the
# to find various numbers in the list

class OrderedList():
    def __init__(self, length: int = 1_000_000) -> None:
        self._elements:List[Dict] = [{'key': x, 'value': x} for x in range(0, length)]

    @property
    def elements(self) -> List[Dict]:
        return self._elements

class RandomList():
    def __init__(self, length: int = 1_000_000) -> None:
        self._elements: List[Dict] = shuffle([{'key': x, 'value': x} for x in range(0, length)])

    @property
    def elements(self) -> List[Dict]:
        return self._elements

def linear_contains(source: List, key: int) -> bool:
    for item in source.elements:
        if(key == item.get('key')):
            return True
    return False

def binary_contains(source: List, key: int) -> bool:
    low: int = 0
    high: int = len(source.elements) - 1

    while(low <= high):
        mid: int = (low + high) // 2
        if source.elements[mid].get('key') < key:
            low = mid + 1
        elif source.elements[mid].get('key') > key:
            high = mid -1
        else:
            return True

    return False




