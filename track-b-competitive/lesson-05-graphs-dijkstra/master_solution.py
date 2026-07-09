"""
Track B — Lesson 5: Graph Theory & Dijkstra's Algorithm

Gap-Filler: represent the graph as an adjacency list (dict of node -> list
of (neighbor, weight)), and use a min-heap (heapq) as a priority queue so we
always expand the closest unvisited node next — O((V + E) log V) instead of
scanning every distance manually each step.
"""

import heapq
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "utils"))
from template_io import read_int, read_ints  # noqa: E402

Graph = dict[int, list[tuple[int, int]]]  # node -> [(neighbor, weight), ...]


def dijkstra(graph: Graph, source: int, n: int) -> list[int]:
    dist = [float("inf")] * n
    dist[source] = 0
    visited: set[int] = set()  # THE FIX lives here — see trap below
    heap: list[tuple[int, int]] = [(0, source)]  # (distance, node)

    while heap:
        d, node = heapq.heappop(heap)

        # ---- THE TRAP: forgetting to track visited nodes ----
        # Without this check, a cyclic graph re-adds already-settled nodes
        # back onto the heap forever every time a cheaper-looking edge is
        # relaxed, and the loop never terminates on a graph with cycles.
        if node in visited:
            continue
        visited.add(node)

        for neighbor, weight in graph.get(node, []):
            if neighbor in visited:
                continue
            new_dist = d + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    return dist


def main() -> None:
    n = read_int()  # number of nodes
    m = read_int()  # number of edges
    graph: Graph = {i: [] for i in range(n)}
    for _ in range(m):
        u, v, w = read_ints()
        graph[u].append((v, w))
        graph[v].append((u, w))  # undirected graph

    source = read_int()
    print(dijkstra(graph, source, n))


if __name__ == "__main__":
    main()
