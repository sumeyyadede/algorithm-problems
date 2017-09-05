#include "SortStack.h"

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
