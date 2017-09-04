#include <iostream>
#include "StackedQueue.h"

using namespace std;

int main(){
	StackedQueue* queue = new StackedQueue;
	cout << queue->pop() << endl;
	cout << queue->pop() << endl;
	cout << "is empty?" << endl;
	cout << queue->isEmpty() << endl;
	queue->push(5);
	queue->push(3);
	queue->push(6);
	cout << "is empty?" << endl;
	cout << queue->isEmpty() << endl;
	cout << queue->pop() << endl;
	cout << queue->pop() << endl;
	queue->push(8);
	cout << queue->peek() << endl;
	cout << queue->pop() << endl;
	cout << queue->pop() << endl;
	cout << queue->pop() << endl;
	cout << queue->pop() << endl;

	// Stack* stack = new Stack();
	// stack->push(1);
	// cout << stack->pop() << endl;

	return 0;
}
