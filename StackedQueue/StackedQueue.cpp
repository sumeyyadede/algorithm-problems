#include "StackedQueue.h"

StackedQueue::StackedQueue(){
	stack1 = new Stack();
	stack2 = new Stack();
	isPushed = false;
}

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
