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
    LinkedList() : head(nullptr) {}

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
};

int main() {
    LinkedList list;

    list.insertAtBeginning(10);
    list.insertAtBeginning(20);
    list.insertAtEnd(30);
    list.insertAtEnd(40);

    std::cout << "Linked List: ";
    list.display();

    return 0;
}