#include "Stack.h"

class StackedQueue{
public:
	StackedQueue();
	int push(int);
	int pop();
	bool isEmpty();
	int peek();
private:
	int moveToStack1();
	int moveToStack2();
	Stack* stack1;
	Stack* stack2;
	bool isPushed;
};
