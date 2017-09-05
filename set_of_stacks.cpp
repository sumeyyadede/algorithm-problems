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

class SetOfStacks {
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

SetOfStacks::SetOfStacks(){	
	_setOfStacks = new Stack<Stack<int>>();
	counter = 0;
	threshold = 3;
	subIndex = -1;	
}

SetOfStacks::~SetOfStacks(){
	delete _setOfStacks;
}

void SetOfStacks::push(int data){
	if(_setOfStacks->isEmpty() || counter == threshold){
		Stack<int>* newStack = new Stack<int>();
		_setOfStacks->push(newStack);
		subIndex = subIndex + 1;
		counter = 0;
	}
	_setOfStacks->peek()->push(new int {data});
	counter = counter + 1;
}

int SetOfStacks::pop(){
	if(!isThereChildStack()){
		return NULL_VALUE;
	}
    int* data = _setOfStacks->peek()->pop();
	counter = counter - 1;
    if(data == NULL){
    	return -1;
    }
	return *data;
}

int SetOfStacks::peek(){
	if(!isThereChildStack()){
		return NULL_VALUE;
	}
	return _setOfStacks->isEmpty() ? NULL_VALUE : *_setOfStacks->peek()->peek();
}

bool SetOfStacks::isEmpty(){
	return _setOfStacks->isEmpty();
}

bool SetOfStacks::isThereChildStack(){
	if(counter==0){
		_setOfStacks->pop();
		if(_setOfStacks->isEmpty()){
			subIndex = -1;
			return false;
		}
		subIndex = subIndex - 1;
		counter = threshold;
	}
	return true;	
}

int SetOfStacks::popAt(int subStack){
	int diff = subIndex - subStack;
	if(diff < 0){
		return NULL_VALUE;
	}
	Stack<Stack<int>>* tempStack = new Stack<Stack<int>>();
	for(int i=0; i < diff; i++){
		tempStack->push(_setOfStacks->pop());
	}
	int data = *_setOfStacks->peek()->pop(); 
	for(int i=0; i < diff; i++){
		_setOfStacks->push(tempStack->pop());
	}
	delete tempStack; 
	return data;
}

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
