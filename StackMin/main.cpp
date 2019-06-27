#include <iostream>
#include "StackMin.h"

using namespace std;

int main(){

	// Node<int> intNode;
	// Node<int> biffy;
	// Node<Node<Node<int>>> nodeNode;
	// Node<int>* mamut;
	// intNode.data = 5;
	// nodeNode.data.data.data = 15;
	// cout << intNode.data << endl;
	// cout << nodeNode.data.data.data << endl;

	// Stack<int>* intStack = new Stack<int>;
	// intStack->push(4);
	// intStack->push(7);
	// intStack->push(5);
	// intStack->push(3);
	// intStack->push(2);
	// cout << intStack->peek() << endl;
	// cout << intStack->pop() << endl;
	// cout << intStack->pop() << endl;
	// cout << intStack->pop() << endl;
	// cout << intStack->pop() << endl;
	// cout << intStack->pop() << endl;
	// cout << intStack->pop() << endl;
	// cout << intStack->isEmpty() << endl;

	StackMin* minStack = new StackMin();
	minStack->push(4);
	minStack->push(8);
	minStack->push(6);
	minStack->push(3);
	minStack->push(8);
	minStack->push(4);
	minStack->push(5);
	cout << minStack->pop() << endl;
	cout << minStack->stackMini() << endl;
	cout << minStack->pop() << endl;
	cout << minStack->stackMini() << endl;
	cout << minStack->pop() << endl;
	cout << minStack->stackMini() << endl;
	cout << minStack->pop() << endl;
	cout << minStack->stackMini() << endl;
	cout << minStack->pop() << endl;
	cout << minStack->stackMini() << endl;
	cout << minStack->pop() << endl;
	cout << minStack->stackMini() << endl;
	cout << minStack->pop() << endl;
	cout << minStack->stackMini() << endl;

	return 0;
}
