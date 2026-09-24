#include <iostream>
using namespace std;

struct Node {
    int value;
    Node* next;
};

class PointerQueue {
private:
    Node* head = nullptr;   //dequeue from here
    Node* tail = nullptr;   //enqueue here
    size_t max_size;
    size_t count = 0;

public:
    PointerQueue(size_t max) : max_size(max) {}

    ~PointerQueue() {
        while (!empty()) dequeue();   //every remaining node needs to be freeeee
    }

    void enqueue(int v) {
        if (full()) {
            cout << "queue is full" << endl;
            return;
        }
        Node* n = new Node;
        n->value = v;
        n->next = nullptr;

        if (empty()) {
            head = n;
            tail = n; //making sure that head and tail are initialised so we can egin
        } else {
            tail->next = n;
            tail = n;
        }
        ++count; //increment count becuse we just added something
    }

    void dequeue() {
        if (empty()) return;
        Node* old = head;
        head = head->next;
        delete old;
        --count;
        if (head == nullptr) tail = nullptr;   // queue just became empty
    }

    int peek() {
        return head->value;   // only call when not empty!
    }

    bool empty() {
        return head == nullptr;
    }

    bool full() {
        return count == max_size;
    }
};

int main() {
    PointerQueue q(3);
    q.enqueue(1);
    q.enqueue(2);
    q.enqueue(3);
    q.enqueue(4);            // prints "queue is full"

    while (!q.empty()) {
        cout << q.peek() << endl;   // prints 1, 2, 3 (first in, first out)
        q.dequeue();
    }
}
