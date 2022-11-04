from typing import Dict, Union, List


class Graph:
    def __init__(self, directed=False) -> None:
        self._adj_mat: Dict[str, List] = {}
        self.directed = directed

    def _add_node(self, node: str) -> None:
        if node not in self._adj_mat:
            self._adj_mat[node] = []

    def add_node(self, nodes: Union[str, int, List]) -> None:
        if isinstance(nodes, str) or isinstance(nodes, int):
            nodes = [nodes]

        for node in nodes:
            self._add_node(node)

    def add_edge(self, node1: str, node2: str) -> None:
        if node1 not in self._adj_mat or node2 not in self._adj_mat:
            raise NameError("yeki az in noda nis to graph")
        self._adj_mat[node1].append(node2)
        if not self.directed:
            self._adj_mat[node2].append(node1)

    def __str__(self):
        result = "Graph \n"
        if len(self._adj_mat) > 0:
            for node in self._adj_mat:
                result += f"{node} ->"
                for item in self._adj_mat[node]:
                    result += f" {item} "
                result += "\n"
        return result

    def isconnected(self):
        pass

    def find_path(self, node1, node2):
        pass

    def shortest_path(self, node1, node2):
        pass


g1 = Graph()

g1.add_node(1)
g1.add_node([2, 3, 4, 5, 6, 7])

g1.add_edge(1, 2)
g1.add_edge(1, 3)
g1.add_edge(1, 4)
g1.add_edge(2, 3)
g1.add_edge(3, 5)
g1.add_edge(4, 5)
g1.add_edge(6, 5)
g1.add_edge(6, 4)

print(g1)
