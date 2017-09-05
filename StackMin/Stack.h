#include "Node.h"

#define NULL_VALUE -1

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

