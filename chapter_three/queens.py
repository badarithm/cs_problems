from typing import List, Dict, Optional
from chapter_three.csp import CSP, Constraint


class QueensConstraint(Constraint[int, int]):
    def __init__(self, columns: List[int]) -> None:
        super().__init__(columns)
        self.columns: List[int] = columns

    def satisfied(self, assignmet: Dict[int, int]) -> bool:
        # q1c = queen 1 column, q1r = queen 1 row
        for q1c, q1r in assignmet.items():
            # q2c = queen 2 column
            for q2c in range(q1c + 1, len(self.columns) + 1):
                if q2c in assignmet:
                    q2r: int = assignmet[q2c] # q2r = queen 2 row
                    if q1r == q2r: # is the same row
                        return False
                    if abs(q1r - q2r) == abs(q1c - q2c): # same diagonal
                        return False

        return True # there is no conflict

def example_search() -> None:
    columns: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    rows: Dict[int, List[int]] = {}
    for column in columns:
        rows[column] = [1, 2, 3, 4, 5, 6, 7, 8]

    csp: CSP[int, int] = CSP(columns, rows)
    csp.add_constraint(QueensConstraint(columns))
    solution: Optional[Dict[int, int]] = csp.backtracking_search()

    if None is solution:
        print("No solution was found!")
    else:
        print(solution)