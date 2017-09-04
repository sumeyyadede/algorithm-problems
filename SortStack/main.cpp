#include <iostream>
#include "SortStack.h"

using namespace std;

int main(){
	
	SortStack* stack = new SortStack();
	cout << stack->isEmpty() << endl;
	stack->push(6);
	stack->push(1);
	stack->push(4);
	stack->push(9);
	stack->push(8);
	stack->push(888);
	cout << stack->isEmpty() << endl;
	cout << stack->peek() << endl;
	cout << stack->pop() << endl;
	cout << stack->pop() << endl;
	cout << stack->pop() << endl;
	cout << stack->pop() << endl;
	cout << stack->peek() << endl;
	cout << stack->pop() << endl;
	cout << stack->pop() << endl;
	cout << stack->pop() << endl;
	cout << stack->pop() << endl;
	cout << stack->pop() << endl;
	cout << stack->pop() << endl;
	cout << stack->pop() << endl;
	cout << stack->peek() << endl;

	return 0;
}
