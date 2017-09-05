#include <iostream>

using namespace std;

#define NULL_VALUE -1

class Node{
public:
	Node(){
		next = NULL;
	}
	int data;
	Node* next;
};

class Stack{
public:
	Stack(){
		head = NULL;
	}
	int push(int);
	int pop();
	bool isEmpty();
	int peek();
private:
	Node* head;
};

int Stack::push(int data){
	Node* node = new Node;
	node->data = data;
	node->next = head;
	head = node;
}
int Stack::pop(){				
	if(isEmpty()){
		return NULL_VALUE;
	}
	int data;
	data = head->data;
	head = head->next;
	return data;
}
bool Stack::isEmpty(){
	return head == NULL;
}
int Stack::peek(){
	if(head != NULL){
		return head->data;
	}
	return NULL_VALUE; 
}

class StackedQueue{
public:
	StackedQueue(){
		stack1 = new Stack();
		stack2 = new Stack();
		isPushed = false;
	}
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

int StackedQueue::moveToStack1(){
	if(!isPushed){
		while(!stack2->isEmpty()){
			stack1->push(stack2->pop());
		}
	isPushed = true;
	}
}
int StackedQueue::moveToStack2(){
	if(isPushed){
		while(!stack1->isEmpty()){
			stack2->push(stack1->pop());
		}
	isPushed = false;
	}
}
int StackedQueue::push(int data){
	moveToStack1();
	stack1->push(data);
}
int StackedQueue::pop(){
	moveToStack2();
	return stack2->pop();
}
bool StackedQueue::isEmpty(){
	return stack1->isEmpty() && stack2->isEmpty();
		
}
int StackedQueue::peek(){
	moveToStack2();
	return stack2->peek();
}	

int main(){
	StackedQueue* queue = new StackedQueue;
	cout << queue->pop() << endl;
	cout << queue->pop() << endl;
	cout << "is empty?" << endl;
	cout << queue->isEmpty() << endl;
	queue->push(5);
	queue->push(3);
	queue->push(6);
	cout << "is empty?" << endl;
	cout << queue->isEmpty() << endl;
	cout << queue->pop() << endl;
	cout << queue->pop() << endl;
	queue->push(8);
	cout << queue->peek() << endl;
	cout << queue->pop() << endl;
	cout << queue->pop() << endl;
	cout << queue->pop() << endl;
	cout << queue->pop() << endl;

	// Stack* stack = new Stack();
	// stack->push(1);
	// cout << stack->pop() << endl;

	return 0;
}
