#include "SetOfStacks.h"

using namespace std;

SetOfStacks::SetOfStacks(){	
	_setOfStacks = new Stack<Stack<int>>();
	counter = 0;
	threshold = 3;
	subIndex = 0;	
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
