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
	delete data;
}

template <class T>
class Stack{
public:
	Stack();
	~Stack();
	void push(T*);
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
	cout << "destructor is on the business" << endl;
	while(!isEmpty()){
		Node<T>* del = head;
		head = head->next;
		delete del;
	}
}
template <class T>
void Stack<T>::push(T* data){
	Node<T>* node = new Node<T>;
	node->data = data;
	node->next = head;
	head = node;
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

class SortStack:public Stack<int>{
public:
	SortStack();
	~SortStack();
	void push(int);
	int pop();
	int peek();
};
SortStack::SortStack(){;}
SortStack::~SortStack(){;}
void SortStack::push(int data){
	if(Stack::isEmpty()){
		Stack::push(new int {data});
		return;
	}
	Stack<int>* tempStack = new Stack<int>();
	while(!Stack::isEmpty() && *Stack::peek() <= ****(new int***{new int**{new int*{new int {data}}}})){
		tempStack->push(Stack::pop());
	}
	Stack::push(new int {data});
	while(!tempStack->isEmpty()){
		Stack::push(tempStack->pop());
	}
	delete tempStack;
}
int SortStack::pop(){
	return Stack::isEmpty() ? NULL_VALUE : *Stack::pop();
}
int SortStack::peek(){
	return Stack::isEmpty() ? NULL_VALUE : *Stack::peek();      
}

void someStackBusiness() {
	Stack<int>* myStack = new Stack<int>();
	myStack->push(new int{1});
	myStack->push(new int{2});
	myStack->push(new int{3});
	myStack->push(new int{4});
	myStack->push(new int{5});
	myStack->push(new int{6});
	myStack->push(new int{7});
	myStack->push(new int{8});
	cout << "bye bye cruel world" << endl;
	delete myStack;
}

int main(){

	someStackBusiness();

	// SortStack* stack = new SortStack();
	// cout << stack->isEmpty() << endl;
	// stack->push(6);
	// stack->push(1);
	// stack->push(4);
	// stack->push(9);
	// stack->push(8);
	// stack->push(888);
	// cout << stack->isEmpty() << endl;
	// cout << stack->peek() << endl;
	// cout << stack->pop() << endl;
	// cout << stack->pop() << endl;
	// cout << stack->pop() << endl;
	// cout << stack->pop() << endl;
	// cout << stack->peek() << endl;
	// cout << stack->pop() << endl;
	// cout << stack->pop() << endl;
	// cout << stack->pop() << endl;
	// cout << stack->pop() << endl;
	// cout << stack->pop() << endl;
	// cout << stack->pop() << endl;
	// cout << stack->pop() << endl;
	// cout << stack->peek() << endl;

	return 0;
}
