from typing import Generic, Iterator, Optional, TypeVar

import matplotlib.pyplot as plt
import networkx as nx

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T, next: Optional["Node[T]"] = None):
        self.value: T = value
        self.next: Optional["Node[T]"] = next

    def __str__(self):
        return f"Node({self.value}) -> [{self.next}]"

    def __repr__(self) -> str:
        return f"Node({self.value},{'NONE' if self.next is None else self.next.__repr__()})"


class LinkedList(Generic[T]):
    def __init__(self):
        self.head: Optional[Node[T]] = None

    def __str__(self):
        return f"LinkedList({self.head})"

    def __repr__(self) -> str:
        return self.__str__()

    def __iter__(self) -> Iterator[T]:
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def insert_at_beginning(self, value: T) -> None:
        new_node = Node[T](value)
        new_node.next = self.head
        self.head = new_node

    def get_last_node(self) -> Node[T]:
        if self.head is None:
            raise RuntimeError("Can't call 'get_last_node' on empty LinkedList.")
        current = self.head
        while current.next is not None:
            current = current.next

        return current

    def insert_at_end(self, value: T) -> None:
        new_node = Node[T](value)
        last_node = self.get_last_node()
        assert last_node.next is None, f"{last_node.next=} != None!"
        last_node.next = new_node


class Graph:
    def __init__(self, n_vertices: int):
        """
        Initialize the graph with the given number of vertices.
        """
        self.vertices = n_vertices
        self.adj_list: dict[int, list[int]] = {i: [] for i in range(n_vertices)}
        self.graph_nx = nx.Graph()  # Create a networkx graph object

    def add_edge(self, u, v) -> None:
        """
        Add an undirected edge between vertex u and vertex v.
        """
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
        self.graph_nx.add_edge(u, v)  # Add edge to the networkx graph

    def get_neighbors(self, u: int) -> list[int]:
        return self.adj_list[u]

    def display(self) -> None:
        """
        Display the graph as an adjacency list.
        """
        for vertex in self.adj_list:
            print(f"{vertex}: {self.adj_list[vertex]}")

    def draw(self) -> None:
        """
        Draw the graph using networkx and matplotlib.
        """
        pos = nx.spring_layout(self.graph_nx)  # Layout for nodes
        nx.draw(
            self.graph_nx,
            pos,
            with_labels=True,
            node_color="blue",
            edge_color="green",
            node_size=1000,
            font_color="white",
        )
        plt.show()

    def __repr__(self):
        return str(self.adj_list)


def main():
    int_llist = LinkedList[int]()
    int_llist.insert_at_beginning(10)
    int_llist.insert_at_beginning(10)
    int_llist.insert_at_beginning(10)
    int_llist.insert_at_beginning(10)
    int_llist.insert_at_beginning(20)

    for i, n in enumerate(int_llist):
        print(i, n)

    print(list(int_llist))
