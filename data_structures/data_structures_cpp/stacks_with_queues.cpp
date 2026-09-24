//implementing stack using queues with C++

//purly to pracitce C++
//stack is LIFO

using namespace std;
#include <queue>
#include <iostream>
#include <utility>


//implementing stack as a queue
class MyStack{
private:
    queue<int> a;
    queue<int> b;
public:
    MyStack() {

    }
    void push(int x){ //O(1) time complexity, O(1) space complex
        b.push(x);

        while (!a.empty()){
            b.push(a.front());
            a.pop();
        }
        swap(a,b);
    }

    int pop(){ //O(n) time complex, O(1) space complex
        int c = a.front();
        a.pop();
        return c;
    }

    int top(){
        return a.front();
    }

    bool empty(){
        return a.empty();

    }
}

//implementing a stack from scratch, no queue

//since we are not using a queue, all of these operations have O(1) space complexity and O(1) time comeplxity
//yay!!
class Stack{
private:
    int top; //this is the index to the top element in the stack
    int arr[100]; //initialises an array to store stack elements 
    //with capacity of 100

public:
    Stack() {top = -1}; 

    //constructor to initialise empty stack

    void push(int x){
        if (!arr.full()){
            arr[++top] = x;
            cout << "added" << x << "to the stack" << endl;
        }
    }

    int pop(){

        if (!arr.empty()){
            return arr[top--];
        }
        else{
            cout << "stack underflow, stack is empty" << endl;
            return 0;
        }
    }

    int peek(){

        if (!arr.empty()){
            return arr[top];
        }
        else{
            cout << "swtack is empty so cannot be peeked" << endl;
        }
    }

    bool full(){
        if (top >= 99){
            cout << "stack is full" << endl;
            return true;
        }
        else{
            return false;
        }
    }

    bool empty(){
        if (top < 0){
            cout << "stack is empty" << endl;
            return true;
        }
        else{
            return false;
        }
    }

}

//now for a stack using pointers specifically
//essentially creating a linked list
struct Node{
    int value;
    Node* next; //points to the node below this one
};

class PointerStack(){
private:
    Node* head = nullptr; //top of stack
    std::size_t count = 09
    std::size_t max_size;

public:
    Stack(std::size_t max) : max_size(max){
        while (!empty()) pop(); //if its not already empty, keep emptying it until it is 
    }

    void push(int val){
        if (full()){
            cout << "stack is full" << endl;
        }
        Node* n = new Node; //make a new node on the heap
        n->value = v;
        n->next = head; //it sits on top opf the old top
        head = n; //it is now the top yayy
        ++count;
    }

    void pop(){
        if (empty()) return;
        Node* old = head; //remembering the top
        head = head->next; //moving it one down
        delete old;
        --count;
        //freeing the old top
    }

    int top(){
        return head->value;
    }

    bool empty(){
        return head == nullptr; //returns true if the head is nullptr meaning the stack is empty
    }

    bool full(){
        return count == max_size;
    }
}