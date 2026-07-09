"""
Track B — Lesson 5 Challenge: Cheapest Flight Route

You're given a network of N airports (numbered 0..N-1) and M direct flights,
each with a cost. Find the cheapest total cost to fly from a given source
airport to a given destination airport. If no route exists, print -1.

Use Dijkstra's algorithm with an adjacency list + heapq. Don't forget to
track visited nodes -- this graph can contain cycles.

Input format:
    N
    M
    M lines, each: u v cost   (an undirected flight between airport u and v)
    source destination

Output format:
    a single integer: cheapest cost, or -1 if unreachable
"""

import heapq
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "utils"))
from template_io import read_int, read_ints  # noqa: E402

Graph = dict[int, list[tuple[int, int]]]


def solve(graph: Graph, n: int, source: int, destination: int) -> int:
    # 📝 TODO: run Dijkstra from `source` using a min-heap of (cost, node).
    # 📝 TODO: track visited nodes so cycles don't cause repeated work.
    # 📝 TODO: return -1 if `destination` is never reached.
    pass


def main() -> None:
    n = read_int()
    m = read_int()
    graph: Graph = {i: [] for i in range(n)}
    for _ in range(m):
        u, v, cost = read_ints()
        graph[u].append((v, cost))
        graph[v].append((u, cost))

    source, destination = read_ints()
    print(solve(graph, n, source, destination))


if __name__ == "__main__":
    main()
