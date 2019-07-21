from __future__ import  annotations
from typing import List, Optional
from chapter_two.generic_search import bfs, Node, node_to_path

MAX_NUM: int = 3

class MCState:
    def __init__(self, missionaries: int, cannibals: int, boat: bool) -> None:
        self.vm: int = missionaries     # west missionaires
        self.vc: int = cannibals        # east cannibals
        self.em: int = MAX_NUM - self.wm # east missionaries
        self.ec: int = MAX_NUM - self.wc # east.cannibals
        self.boat: bool = boat

    def goal_test(self) -> bool:
        return self.is_legal and self.em == MAX_NUM and self.ec == MAX_NUM

    def __str__(self) -> str:
        print(
            """On the west bank there are {} missionaries and {} cannibals.
               On the east bank there are () missionaries and {} cannibals.
               The boat is one the {} bank. 
            """.format(self.wm, self.wc, self.em, self.ec, ("west" if self.boat else "east")))

    @property
    def is_legal(self) -> bool:
        if self.vm < self.wc and self.wm > 0:
            return False

        if self.em < self.ec and self.em > 0:
            return False

        return True

    def successors(self) -> List[MCState]:
        sucs: List[MCState] = []

        if self.boat:
            if self.wm > 1:
                sucs.append()