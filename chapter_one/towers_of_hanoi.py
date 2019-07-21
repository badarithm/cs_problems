from typing import TypeVar, Generic, List, Mapping

T = TypeVar("T")

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

    def __repr__(self):
        return repr(self._container)


num_discs: int = 3
tower_a: Stack[int] = Stack()
tower_b: Stack[int] = Stack()
tower_c: Stack[int] = Stack()

for i in range(1, num_discs + 1):
    # push three disks to initial tower
    tower_a.push(i)

def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int) -> None:
    print('---------------- START')
    print(begin)
    print(end)
    print(temp)
    print(n)
    print('---------------- END')
    if 1 == n :
        end.push(begin.pop())
    else:
        hanoi(begin, temp, end, n - 1)
        hanoi(begin, end, temp, 1)
        hanoi(temp, end, begin, n - 1)


class Hanoi():
    def __init__(self, disks: int = 1, towers: int = 3) -> None:
        self._disk_number = disks
        self._tower_number = towers
        self.prepareDisks()

    def prepareTowers(self):
        for i in range(1, self._tower_number + 1):
            self.towers.append()

    def prepareDisks(self) -> None:
        for i in range(1, self._disks + 1):
            self._tower_a.push(i)


    def solve(self):
        pass


