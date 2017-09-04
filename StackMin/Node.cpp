#include "Node.h"

template <class T>
Node<T>::Node(){
	next = NULL;
}
template <class T>
Node<T>::~Node(){
	delete data;;
}
