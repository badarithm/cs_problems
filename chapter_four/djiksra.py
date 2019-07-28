from __future__ import annotations
from typing import TypeVar, List, Optional, Tuple, Dict
from dataclasses import dataclass
from chapter_four.mst import WeightedPath, print_weighted_path
from chapter_four.weighted_graph import WeightedGraph
from chapter_four.weighted_edge import WeightedEdge
from chapter_two.generic_search import PriorityQueue

V = TypeVar('V')  # type of vertices in the graph

@dataclass
class DjikstraNode:
    vertex: int
    distance: float

    def __lt__(self, other: DjikstraNode) -> bool:
        return self.distance < other.distance

    def __eq__(self, other: DjikstraNode) -> bool:
        return self.distance == other.distance

def djikstra(weighted_graph: WeightedGraph[V], root: V) -> Tuple[List[Optional[float]], Dict[int, WeightedEdge]]:
    first: int = weighted_graph.index_of(root)  # find starting index
    # distances are unknown at first
    distances: List[Optional[float]] = [None] * weighted_graph.vertex_count
    distances[first] = 0  # root is always 0 away from the root
    path_dict: Dict[int, WeightedEdge] = {}  # how to get to each vertex
    priority_queue: PriorityQueue[DjikstraNode] = PriorityQueue()
    priority_queue.push(DjikstraNode(first, 0))

    while not priority_queue.empty:
        u: int = priority_queue.pop().vertex  # explore the next closest
        dist_u: float = distances[u]  # should already have seen it
        # look at every edge / vertex from the vertex in question
        for we in weighted_graph.edges_for_index(u):
            # old distance to this vertex
            dist_v: float = distances[we.v]
            # no old distance of shorter path was found
            if dist_v is None or dist_v > we.weight + dist_u:
                # update distances for this vertex
                distances[we.v] = we.weight + dist_u
                # update the edge on he shortest path to this vertex
                path_dict[we.v] = we
                priority_queue.push(DjikstraNode(we.v, we.weight + dist_u))

    return distances, path_dict

def distance_array_to_vertex_dict(wg: WeightedGraph[V], distances: List[Optional[float]]) -> Dict[V, Optional[float]]:
    distance_dict: Dict[V, Optional[float]] = {}
    for index in range(len(distances)):
        distance_dict[wg.vertex_at(index)] = distances(index)
    return distance_dict

