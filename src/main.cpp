#include <functional>
#include <iostream>

struct Node {
    int data;
    Node *next;

    Node(int value) : data(value), next(nullptr) {}
};

class LinkedList {
private:
    Node *head;

public:
    LinkedList() : head(0) {}

    ~LinkedList() {
        Node *current = head;
        Node *next;
        while (current != nullptr) {
            next = current->next;
            delete current;
            current = next;
        }
    }

    void insertAtBeginning(int value) {
        Node *newNode = new Node(value);
        newNode->next = head;
        head = newNode;
    }

    void insertAtEnd(int value) {
        Node *newNode = new Node(value);
        newNode->next = nullptr;

        if (head == nullptr) {
            head = newNode;
        } else {
            Node *temp = head;
            while (temp->next != nullptr) {
                temp = temp->next;
            }
            temp->next = newNode;
        }
    }

    void display() const {
        Node *temp = head;
        while (temp != nullptr) {
            std::cout << temp->data << " -> ";
            temp = temp->next;
        }
        std::cout << "NULL" << std::endl;
    }

    Node *getHead() const { return head; }

    int accumulate(std::function<int(int)> func) const {
        int sum = 0;
        Node *temp = head;
        while (temp != nullptr) {
            sum += func(temp->data);
            temp = temp->next;
        }
        return sum;
    };
};

int main() {
    LinkedList list;

    list.insertAtBeginning(10);
    list.insertAtBeginning(-10);
    list.insertAtEnd(30);
    list.insertAtEnd(40);

    std::cout << "Linked List: ";
    list.display();

    Node *secondNode = list.getHead();

    if (secondNode != nullptr) {
        secondNode = secondNode->next;
    }

    LinkedList newList;

    while (secondNode != nullptr) {
        newList.insertAtEnd(secondNode->data);
        secondNode = secondNode->next;
    }
    newList.display();

    int sumOfSquares = list.accumulate([](int x) { return x * x; });
    printf("%d\n", sumOfSquares);
    int sumOfAllNodes = list.accumulate([](int x) { return x; });
    printf("%d\n", sumOfAllNodes);

    return 0;
}