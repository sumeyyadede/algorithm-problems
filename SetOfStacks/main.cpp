#include <iostream>
#include "SetOfStacks.h"

using namespace std;

int main(){

	SetOfStacks* stack = new SetOfStacks();
	cout << "isEmpty" << stack->isEmpty() << endl;
	stack->push(6);
	stack->push(1);
	stack->push(4);
	stack->push(9);
	stack->push(8);
	stack->push(888);
	stack->push(49);
	stack->push(94);
	stack->push(56);
	stack->push(87);
	cout << "isEmpty " << stack->isEmpty() << endl;
	cout << stack->peek() << endl;
	cout << "popAt " << stack->popAt(0) << endl;
	cout << stack->pop() << endl;
	cout << stack->pop() << endl;
	cout << "popAt " << stack->popAt(5) << endl;
	cout << stack->pop() << endl;
	cout << stack->pop() << endl;
	cout << "peek " << stack->peek() << endl;
	cout << stack->pop() << endl;
	cout << "popAt " << stack->popAt(1) << endl;
	cout << stack->pop() << endl;
	cout << stack->pop() << endl;
	cout << stack->pop() << endl;
	cout << stack->pop() << endl;
	cout << stack->pop() << endl;
	cout << "peek " << stack->peek() << endl;
	cout << stack->pop() << endl;
	cout << stack->pop() << endl;
	cout << "peek " << stack->peek() << endl;
	cout << stack->pop() << endl;

	return 0;
}
