from typing import Generic, Iterator, Optional, TypeVar

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


if __name__ == "__main__":
    main()
