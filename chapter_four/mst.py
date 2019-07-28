from typing import Optional, List, TypeVar
from chapter_four.weighted_graph import WeightedGraph
from chapter_four.weighted_edge import WeightedEdge
from chapter_two.generic_search import PriorityQueue
from enum import Enum

""" Jarniks algorithm: find shortest path for a graph"""

V = TypeVar('V') # Type of vertices in the graph
WeightedPath = List[WeightedEdge]


class Station(Enum):
    SEATTLE = "Seattle"
    SAN_FRANCISCO = "San Francisco"
    LOS_ANGELES = "Los Angeles"
    RIVERSIDE = "Riverside"
    PHOENIX = "Phoenix"
    CHICAGO = "Chicago"
    BOSTON = "Boston"
    NEW_YORK = "New York"
    ATLANTA = "Atlanta"
    MIAMI = "Miami"
    DALLAS = "Dallas"
    HOUSTON = "Houston"
    DETROIT = "Detroit"
    PHILADELPHIA = "Philadelphia"
    WASHINGTON = "Washington"

    @classmethod
    def list(cls):
        return list(map(lambda city: city.value, cls))

def total_weight(path: WeightedPath):
    return sum([e.weight for e in path])


def mst(wg: WeightedGraph[V], start: int = 0) -> Optional[WeightedPath]:
    if start > (wg.vertex_count - 1) or 0 > start:
        return None
    result: WeightedPath = []  # holds the final mst
    priority_queue: PriorityQueue[WeightedEdge] = PriorityQueue()
    visited: [bool] = [False] * wg.vertex_count # where we have been

    def visit(index: int):
        visited[index] = True  # mark as visited
        for edge in wg.edges_for_index(index):
            # add all edges coming from here to pq
            if not visited[edge.v]:
                priority_queue.push(edge)
    visit(start)
    while not priority_queue.empty:  # keep going unless there is nothing left
        edge = priority_queue.pop()
        if visited[edge.v]:
            continue  # don't revisit
        # this is current smallest, so add it to solution
        result.append(edge)
        visit(edge.v)  # visit where this connects
    return result


# just print and do nothing else
def print_weighted_path(weighted_graph: WeightedGraph, weighted_path: WeightedPath) -> None:
    for edge in weighted_path:
        print(f"{weighted_graph.vertex_at(edge.u)} {edge.weight} > {weighted_graph.vertex_at(edge.v)}")
    print(f"Total Weight: {total_weight(weighted_path)}")


# example with hyperloop stations
def hyperloop_test():
    city_graph2: WeightedGraph[str] = WeightedGraph(Station.list())

    city_graph2.add_edge_by_vertices(Station.SEATTLE, Station.CHICAGO, 1737)
    city_graph2.add_edge_by_vertices(Station.SEATTLE, Station.SAN_FRANCISCO, 678)
    city_graph2.add_edge_by_vertices(Station.SAN_FRANCISCO, Station.RIVERSIDE, 386)
    city_graph2.add_edge_by_vertices(Station.SAN_FRANCISCO, Station.LOS_ANGELES, 348)
    city_graph2.add_edge_by_vertices(Station.LOS_ANGELES, Station.RIVERSIDE, 50)
    city_graph2.add_edge_by_vertices(Station.LOS_ANGELES, Station.PHOENIX, 357)
    city_graph2.add_edge_by_vertices("Riverside", Station.PHOENIX, 307)
    city_graph2.add_edge_by_vertices("Riverside", "Chicago", 1704)
    city_graph2.add_edge_by_vertices("Phoenix", "Dallas", 887)
    city_graph2.add_edge_by_vertices("Phoenix", "Houston", 1015)
    city_graph2.add_edge_by_vertices("Dallas", "Chicago", 805)
    city_graph2.add_edge_by_vertices("Dallas", "Atlanta", 721)
    city_graph2.add_edge_by_vertices("Dallas", "Houston", 225)
    city_graph2.add_edge_by_vertices("Houston", "Atlanta", 702)
    city_graph2.add_edge_by_vertices("Houston", "Miami", 968)
    city_graph2.add_edge_by_vertices("Atlanta", "Chicago", 588)
    city_graph2.add_edge_by_vertices("Atlanta", "Washington", 543)
    city_graph2.add_edge_by_vertices("Atlanta", "Miami", 604)
    city_graph2.add_edge_by_vertices("Miami", "Washington", 923)
    city_graph2.add_edge_by_vertices("Chicago", "Detroit", 238)
    city_graph2.add_edge_by_vertices("Detroit", "Boston", 613)
    city_graph2.add_edge_by_vertices("Detroit", "Washington", 396)
    city_graph2.add_edge_by_vertices("Detroit", "New York", 482)
    city_graph2.add_edge_by_vertices("Boston", "New York", 190)
    city_graph2.add_edge_by_vertices("New York", "Philadelphia", 81)
    city_graph2.add_edge_by_vertices("Philadelphia", "Washington", 123)

    result: Optional[WeightedPath] = mst(city_graph2)
    if result is None:
        print("No solution found")
    else:
        print_weighted_path(city_graph2, result)