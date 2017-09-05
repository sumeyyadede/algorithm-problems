#include "StackMin.h"

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
