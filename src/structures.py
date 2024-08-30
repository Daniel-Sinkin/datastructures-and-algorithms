from typing import Generic, Iterator, NamedTuple, Optional, TypeVar

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

    @staticmethod
    def run_template() -> None:
        print("\nLinkedList Template")
        int_llist = LinkedList[int]()
        int_llist.insert_at_beginning(10)
        int_llist.insert_at_beginning(10)
        int_llist.insert_at_beginning(10)
        int_llist.insert_at_beginning(10)
        int_llist.insert_at_beginning(20)

        for i, n in enumerate(int_llist):
            print(i, n)

        print(list(int_llist))


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


class POS(NamedTuple):
    y: int
    x: int


class Grid(Generic[T]):
    def __init__(self, grid: list[list[T]]):
        self.grid: list[list[T]] = grid

    def __repr__(self) -> str:
        return f"Grid({self.grid})"

    def __str__(self) -> str:
        return "\n".join([str(row) for row in self.grid])

    @property
    def empty(self) -> bool:
        return len(self.grid) == 0

    @property
    def shape(self) -> tuple[int, int]:
        if self.empty:
            return True
        else:
            return (len(self.grid), len(self.grid[0]))

    @property
    def y_size(self) -> int:
        return self.shape[0]

    @property
    def x_size(self) -> int:
        return self.shape[1]

    def is_valid(self) -> bool:
        if self.empty:
            return True

        first_row = self.grid[0]
        for row in self.grid[1:]:
            if len(row) != len(first_row):
                return False

        return True

    def is_position_valid(self, pos: POS) -> bool:
        return (self.y_size > pos.y >= 0) and (self.x_size > pos.x >= 0)

    def get(self, pos: POS) -> T:
        assert self.is_position_valid(pos)
        return self.grid[pos.y][pos.x]

    def set(self, pos: POS, val: T) -> None:
        assert self.is_position_valid(pos)
        self.grid[pos.y][pos.x] = val

    def get_neighbors(self, pos: POS) -> list[POS]:
        potential_neighbors: list[POS] = [
            POS(pos.y - 1, pos.x),
            POS(pos.y + 1, pos.x),
            POS(pos.y, pos.x - 1),
            POS(pos.y, pos.x + 1),
        ]
        return [
            nb
            for nb in potential_neighbors
            if self.is_position_valid(nb) and self.get(pos) == self.get(nb)
        ]

    def BFS(self, starting_node: POS) -> list[POS]:
        assert self.is_valid(), f"Invalid {self=}."
        assert self.is_position_valid(starting_node), f"Invalid {starting_node=}."

        seen_positions: list[POS] = [starting_node]
        positions_to_check = self.get_neighbors(starting_node)
        while len(positions_to_check) > 0:
            curr = positions_to_check.pop()

            if curr not in seen_positions:
                seen_positions.append(curr)
                new_positions = self.get_neighbors(curr)
                positions_to_check += new_positions

        return seen_positions

    @staticmethod
    def run_template() -> None:
        print("\nGrid Template")
        grid_data: list[list[int]] = [
            [1, 0, 1, 1, 0],
            [0, 1, 0, 0, 0],
            [1, 1, 1, 1, 1],
            [0, 0, 1, 0, 1],
            [1, 0, 0, 0, 0],
        ]
        grid = Grid(grid_data)
        print(grid)

        for pos in grid.BFS(POS(2, 2)):
            grid.set(pos, 2)

        print()
        print(grid)

        for pos in grid.BFS(POS(0, 4)):
            grid.set(pos, 3)

        print()
        print(grid)


def main():
    LinkedList.run_template()
    Grid.run_template()


if __name__ == "__main__":
    main()
