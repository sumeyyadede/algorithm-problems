#include <iostream>

using namespace std;

#define NULL_VALUE -1

template <class T>
class Node{
public:
	Node();
	~Node();
	T* data;               
	Node* next;
};

template <class T>
Node<T>::Node(){
	next = NULL;
}
template <class T>
Node<T>::~Node(){
	delete data;;
}

template <class T>
class Stack{
public:
	Stack();
	~Stack();
	Node<T>* push(T*);
	T* pop();
	bool isEmpty();
	Node<T>* peekNode();
	T* peek();
private:
	Node<T>* head;
};

template <class T>
Stack<T>::Stack(){
	head = NULL;
}
template <class T>
Stack<T>::~Stack(){
	while(!isEmpty()){
		Node<T>* del = head;
		head = head->next;
		delete del;
	}
}
template <class T>
Node<T>* Stack<T>::push(T* data){
	Node<T>* node = new Node<T>;
	node->data = data;
	node->next = head;
	head = node;
	return head;
}
template <class T>
T* Stack<T>::pop(){				
	if(isEmpty()){    
		return NULL;
	}
	T* data;
	data = head->data;
	head = head->next;
	return data;
}
template <class T>
bool Stack<T>::isEmpty(){
	return head == NULL;
}
template <class T>
Node<T>* Stack<T>::peekNode(){
	return head;
}
template <class T>
T* Stack<T>::peek(){
	return Stack::isEmpty() ? NULL : head->data;
}

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

StackMin::StackMin(){
	_stackMin = new Stack<Node<int>>();      
}
StackMin::~StackMin(){
	delete  _stackMin;     
}
int StackMin::push(int data){
	Node<int>* n = Stack::push(new int {data});
	if(_stackMin->isEmpty() || *_stackMin->peek()->data > *n->data){
		_stackMin->push(n);
	}
}
int StackMin::pop(){
	if (Stack::peekNode() == _stackMin->peek()){
		_stackMin->pop();
	}
	return *Stack::pop();
}
int StackMin::stackMini(){
	return _stackMin->isEmpty() ? NULL_VALUE : *_stackMin->peek()->data; 
}

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

	StackMin* minStack = new StackMin;
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
