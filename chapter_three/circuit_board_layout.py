from typing import NamedTuple, List, Dict, Optional, TypeVar
from random import choice
from string import  ascii_uppercase
from chapter_three.csp import CSP, Constraint

Grid = List[List[str]]

V = TypeVar("V") # variable type
D = TypeVar("D") # domain type

class GridLocation(NamedTuple):
    row: int
    column: int

class Component(GridLocation):
    @property
    def area(self):
        return self.row * self.column

class Board:
    def __init__(self, width: int = 10, height: int = 10):
        self._width: int = width
        self._height: int = height

    @property
    def area(self):
        return self._height * self._width
# will generate a number of squares that have area equal or smaller than the total borad area

def generate_domain(heigth:int = 10, width: int = 10, cover: float = 0.6):
    domain: List[Component] = []


def solve():
    board: Board = generate_domain(10, 10)
    components: List[Component] = [Component(1, 6), Component(4, 4), Component(3, 3), Component(2,2), Component(2, 5)]

    area_component: int = sum([component.area for component in components])
    board_area = board.area
    if  area_component > board_area:
        print("Bord area {} is smaller than component total area {}. There is no solution".format(area_component, board_area))
    else :
