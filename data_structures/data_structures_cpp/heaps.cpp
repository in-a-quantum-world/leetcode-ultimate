//heaps as vectors

//a heap is always a complete binry tree, meanin every level is full except perjaps the alst 
// push is bubble up, pop is bubble down 
//for bubble up, if it is smaller than its parent, keep swapping untilit isnt
//for bubble down you cannot delete index 0 since that would leave a hole. instead
//movethe last item into the root and then swap it downwards with its smaler chil until both children are bigger. it has to be the smaller chidl since if you swapped with the bigger one, that bigger child
//would become the parent of the smaller one, thus breaking the rule

//both push and pop operations are O(log n) and finding the top one is O(1)

#include <iostream>
#include <stdexcept>
#include <utility>
#include <vector>
using namespace std;

class MinHeap {
private:
    vector<int> data;   // the tree, stored level by level

    int parent(int i) { return (i - 1) / 2; }
    int left(int i)   { return 2 * i + 1; }
    int right(int i)  { return 2 * i + 2; }

    // New item at the bottom: swap it up while it's smaller than its parent.
    void siftUp(int i) {
        while (i > 0 && data[i] < data[parent(i)]) {
            swap(data[i], data[parent(i)]);
            i = parent(i);
        }
    }

    // Item at position i may be too big: swap it down with its smaller child.
    void siftDown(int i) {
        int n = data.size();
        while (true) {
            int smallest = i;
            int l = left(i);
            int r = right(i);
            if (l < n && data[l] < data[smallest]) smallest = l;
            if (r < n && data[r] < data[smallest]) smallest = r;
            if (smallest == i) break;    // both children are bigger: done
            swap(data[i], data[smallest]);
            i = smallest;
        }
    }

public:
    void push(int v) {
        data.push_back(v);               // add at the next free spot
        siftUp(data.size() - 1);         // restore the heap property
    }

    void pop() {
        if (empty()) throw out_of_range("pop on empty heap");
        data[0] = data.back();           // move the last item to the root
        data.pop_back();
        if (!empty()) siftDown(0);       // restore the heap property
    }

    int top() {
        if (empty()) throw out_of_range("top on empty heap");
        return data[0];                  // smallest item is always at the root
    }

    bool empty() { return data.empty(); }
    int size()   { return data.size(); }
};

int main() {
    MinHeap h;
    for (int x : {5, 3, 8, 1, 9, 2}) h.push(x);

    while (!h.empty()) {
        cout << h.top() << ' ';          // prints 1 2 3 5 8 9
        h.pop();
    }
    cout << '\n';
}