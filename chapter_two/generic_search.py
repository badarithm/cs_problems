# this was solved before
from __future__ import  annotations
from typing import TypeVar, Iterable, Sequence, Generic, List, Callable, Set, Deque, Dict, Any, Optional
from typing_extensions import Protocol
from functools import total_ordering
from heapq import heappop, heappush
from math import sqrt
from chapter_two.maze_location import MazeLocation

T = TypeVar("T")

def linear_contains(interable: Iterable[T], key: T) -> bool:
    for item in interable:
        if key == item:
            return True

    return False

def euclidean_distance(goal: MazeLocation) -> Callable[[MazeLocation], float]:
    def distance(ml: MazeLocation) -> float:
        x_dist: int = ml.column - goal.column
        y_dist: int = ml.row - goal.row
        return sqrt(x_dist ** 2 + y_dist ** 2)
    return distance # so it is like a partially applied function

def manhattan_distance(goal: MazeLocation) -> Callable[[MazeLocation], float]:
    def distance(ml: MazeLocation) -> float:
        x_dist: int = abs(ml.column - goal.column)
        y_dist: int = abs(ml.row - goal.row)
        return (x_dist + y_dist)
    return distance

def astar(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]], heuristic: Callable[[T], float]) -> Optional[Node[T]]:
    # frontier is where we've yet to go
    frontier: PriorityQueue[Node[T]] = PriorityQueue()
    frontier.push(Node(initial, None, 0.0, heuristic(initial)))
    # explored is where we've been
    explored: Dict[T, float] = {initial, 0.0}

    # keep going while there is more to explore
    while not frontier.empty:
        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state

        # if goal was found then we're done
        if(goal_test(current_state)):
            return current_node

        for child in successors(current_state):
            new_cost: float = current_node.cost + 1 # 1 here assumes a grid, use different cost function for more sophisticated cases

            if child not in explored or explored[child] > new_cost:
                explored[child] = new_cost
                frontier.push(Node(child, current_node, new_cost, heuristic(child)))
    return None

class Queue(Generic[T]):
    def __init__(self) -> None:
        self._container: Deque[T] = Deque() #his does not work

    @property
    def empty(self):
        return not self._container

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.popleft()

    def __repr__(self):
        return repr(self._container)


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    @property
    def empty(self) -> bool:
        return not self._container

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

    def __repr__(self):
        return repr(self._container)

class PriorityQueue(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    @property
    def empty(self):
        return not self._container

    def push(self, item: T) -> None:
        heappush(self._container, item) # priority determined by order of item

    def pop(self) -> T:
        return heappop(self._container) # out by priority

    def __repr__(self):
        return repr(self._container)

class Node(Generic[T]):
    def __init__(self, state: T, parent: Optional[Node[T]], cost: float = 0.0, heuristic: float = 0.0) -> None:
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    @property
    def weight(self):
        return self.cost + self.heuristic

    def __lt__(self, other):
        return self.weight < other.weight

class PriorityQueue(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    @property
    def empty(self) -> bool:
        return not self._container

    def push(self, item: T) -> None:
        heappush(self._container, item)

    def pop(self) -> T:
        return heappop(self._container)

    def __repr__(self) -> str:
        return repr(self._container)

def dfs(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]]) -> Optional[Node[T]]:
    frontier: Stack[Node[T]] = Stack()
    frontier.push(Node(initial, None))

    explored: Set[T] = {initial}
    # keep looking while frontier is not empty
    while not frontier.empty:
        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state
        # if we found the goal then we're done
        if goal_test(current_state):
            return current_node

        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child, current_state))
    return None

def bfs(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]]) -> Optional[Node[T]]:
    frontier: Queue[Node[T]] = Queue()
    frontier.push(Node(initial, None))

    explored: Set[T] = {initial}
    while not frontier.empty:
        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state
        if goal_test(current_state):
            return current_node

        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child, current_node))

    return None


def node_to_path(node: Node[T]) -> List[T]:
    path: List[T] = []
    if node is not None:
        path = [node.state]

        while node.parent is not None:
            node = node.parent
            path.append(node.state)
        path.reverse()
    return path

def astar(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]], heuristic: Callable[[T], float]) -> Optional[Node[T]]:
    frontier: PriorityQueue[Node[T]] = PriorityQueue()
    frontier.push(Node(initial, None, 0.0, heuristic(initial)))

    explored: Dict[T, float] = {initial: 0.0}
    while not frontier.empty:
        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state

        if goal_test(current_state):
            return current_node
        for child in successors(current_state):
            new_cost: float = current_node.cost + 1
            if child not in explored or explored[child] > new_cost:
                explored[child] = new_cost
                frontier.push(Node(child, current_node, new_cost, heuristic(child)))
    return None



