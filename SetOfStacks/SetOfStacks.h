#include "Stack.h"

class SetOfStacks:public Stack<int>{
public:
	SetOfStacks();
	~SetOfStacks();
	void push(int);
	int pop();
	int peek();
	bool isEmpty();
	int popAt(int);
private:
	Stack<Stack<int>>* _setOfStacks;
	bool isThereChildStack();
	int counter;
	int threshold;
	int subIndex;
};
