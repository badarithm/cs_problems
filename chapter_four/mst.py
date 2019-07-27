from typing import Optional, List, TypeVar
from chapter_four.weighted_graph import WeightedGraph
from chapter_four.weighted_edge import WeightedEdge
from chapter_two.generic_search import PriorityQueue

V = TypeVar('V') # Type of vertices in the graph
WeightedPath = List[WeightedEdge]

