using namespace std;

#include <iostream>
#include <utilities>

class PointerQueue(){
    
private:
    Node* head = nullptr;
    Node* tail = nullptr;
    std::size_t max_size;
    std::size_t count = 0;

public:
    Stack(std::size_t max) : max_size(max){
        while (!empty()) pop(); //if its not already empty, keep emptying it until it is
    }

    void enqueue(){
        if (!full()){
            Node* n = new Node; //make a new node on the heap
            n->value = v;
            n->next = head; //it sits on top opf the old top
            head = n; //it is now the top yayy
            ++count;
        }

        else{
            cout << "queue is full" << endl;
        }
    }

    void dequeue(){
        if (!empty()){
            Node* old = head; //remembering the top
            head = head->next; //moving it one down
            delete old;
            --count;
        }

    }

    int peek(){
        return head->value;
    }
    bool empty(){
        if (head == nullptr && tail == nullptr){
            return true;
        }
        else{
            return false;
        }
    }

    bool full(){
        if (count == max_size){
            return true;
        }
        else{
            return false;
        }
        
    }


};















struct Node(){
    int value;
    Node* next
};


class Queue()