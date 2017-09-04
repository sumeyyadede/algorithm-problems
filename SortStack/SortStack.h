#include "Stack.h"

class SortStack:public Stack<int>{
public:
	SortStack();
	~SortStack();
	void push(int);
	int pop();
	int peek();
};
