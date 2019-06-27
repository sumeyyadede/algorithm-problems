#include "Node.h"
#define NULL_VALUE -1

class Stack{

public:
	Stack();
	int push(int);
	int pop();
	bool isEmpty();
	int peek();

private:
	Node* head;

};
