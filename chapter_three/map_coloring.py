from chapter_three.csp import Constraint, CSP
from typing import Dict, List, Optional

class MapColoringConstraint(Constraint[str, str]):

    def __init__(self, place_one: str, place_two: str) -> None:
        super().__init__([place_one, place_two]) # same as Constraint.__init__([place_one, place_two])
        self.place_one: str = place_one
        self.place_two: str = place_two

    def satisfied(self, assignment: Dict[str, str]) -> bool:
        # if either place is not in the assignment then it is not
        # yet possile for their colors to be conflicting
        if self.place_one not in assignment or self.place_two not in assignment:
            return True

        # check if the color assigned to place one is not the same as color two
        return assignment[self.place_one] != assignment[self.place_two]


# in the book they are using if __name__ == "__main__", but that rarely works for me

variables: List[str] = ["Western Australia", "Northern Territory", "South Australia",
                        "Queensland", "New South Wales", "Victoria", "Tasmania"]

domains: Dict[str, List[str]] = {}
for variable in variables:
    domains[variable] = ["red", "green", "blue"]
    csp