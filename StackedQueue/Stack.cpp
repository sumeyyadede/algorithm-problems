#include "Stack.h"

Stack::Stack(){
	head = NULL;
}

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
