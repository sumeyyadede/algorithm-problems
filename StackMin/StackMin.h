#include "Stack.h"

class StackMin:public Stack<int>{
public:
	StackMin();
	~StackMin();
	int push(int);
	int pop();
	int stackMini();

private:
	Stack<Node<int>>* _stackMin;
};
