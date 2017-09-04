#include "Stack.h"

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
