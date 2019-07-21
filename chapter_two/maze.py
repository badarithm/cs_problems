from enum import Enum
from typing import List, NamedTuple, Callable, Optional
import random
from math import sqrt
from chapter_two.generic_search import dfs, bfs, node_to_path, Node, astar, manhattan_distance, euclidean_distance
from chapter_two.maze_location import MazeLocation

class Cell(str, Enum):
    EMPTY = ""
    BLOCKED = "X"
    START = "S"
    GOAL = "G"
    PATH = "P"

class Maze:
    def __init__(self, rows: int, columns: int, start: MazeLocation = MazeLocation(0, 0), goal: MazeLocation = MazeLocation(9, 9)) -> None:
        self._rows: int = rows
        self._columns: int = columns
        self._start: MazeLocation = start
        self._goal: MazeLocation = goal
        self._grid: List[List[Cell]] = [[Cell.EMPTY for c in range(0, self._columns)] for r in range(0, self._rows)]


    def randomly_fill(self, rows: int, columns: int, spareseness: float):
        for row in range(rows):
            for column in range(columns):
                if random.uniform(0, 1.0) < spareseness:
                    self._grid[row][column] = Cell.BLOCKED
                else :
                    self._grid[row][column] = Cell.EMPTY

    @property
    def initial(self):
        return self._start

    def successors(self, m_location: MazeLocation) -> List[MazeLocation]:
        locations: List[MazeLocation] = []

        # checking above
        if m_location.row + 1 < self._rows and self._grid[m_location.row + 1][m_location.column] != Cell.BLOCKED :
            locations.append(MazeLocation(m_location.row + 1, m_location.column))
        # checking below
        if m_location.row - 1 >= 0 and self._grid[m_location.row - 1][m_location.column] != Cell.BLOCKED:
            locations.append(MazeLocation(m_location.row - 1, m_location.column))

        # checking to the right
        if m_location.column + 1  < self._columns and self._grid[m_location.row][m_location.column + 1] != Cell.BLOCKED:
            locations.append(MazeLocation(m_location.row, m_location.column + 1))

        # checking to the left
        if m_location.column - 1 >=  0 and self._grid[m_location.row][m_location.column - 1] != Cell.BLOCKED:
            locations.append(MazeLocation(m_location.row, m_location.column - 1))

        return locations

    def mark(self, path: List[MazeLocation]) -> None:
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = Cell.PATH
            self._grid[self._start.row][self._start.column] = Cell.START
            self._grid[self._goal.row][self._goal.column] = Cell.GOAL

    def clear(self, path: List[MazeLocation]) -> None:
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = Cell.EMPTY
        self._grid[self._start.row][self._start.column] = Cell.START
        self._grid[self._goal.row][self._goal.column] = Cell.GOAL

    def __str__(self) -> str:
        output: str = ""
        for row in self._grid:
            output += " ".join([c.value for c in row]) + "\n"
        return output

    def solve_dfs(self):
        return dfs(self.initial, self.goal_test, self.successors)
        self.print_solution(solution)

    def solve_bfs(self):
        return bfs(self.initial, self.goal_test, self.successors)
        self.print_solution(solution)

    def solve_astar(self) -> None:
        distance: Callable[[MazeLocation], float] = manhattan_distance(self._goal)
        solution = astar(self.initial, self.goal_test, self.successors, distance)
        if solution is None:
            print('No sulution found using A*!')
        else:
            self.print_solution(solution)

    def print_solution(self, solution: Optional[Node[MazeLocation]]) -> None:
        if solution is None:
            print('Solution does not exist')
        else:
            path = node_to_path(solution)
            self.mark(path)
            print(self)

    def goal_test(self, ml: MazeLocation) -> bool:
        return ml == self._goal