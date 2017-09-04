#include <cstddef>
#include <iostream>

template <class T>
class Node{
public:
	Node();
	~Node();
	T* data;               
	Node* next;
};
