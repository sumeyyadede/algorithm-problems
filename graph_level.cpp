#include <iostream>
#include <map>

#define NULL_VALUE -1

using namespace std;

template <class T>
class Node{
public:
	Node();
	~Node();
	T* data;               
	Node* next;
};

template <class T>
Node<T>::Node(){
	next = NULL;
}
template <class T>
Node<T>::~Node(){
	delete data;
}

template <class T>
class Stack{
public:
	Stack();
	~Stack();
	void push(T*);
	T* pop();
	bool isEmpty();
	Node<T>* peekNode();
	T* peek();
private:
	Node<T>* head;
};

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
	Node<T>* node = new Node<T>();
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

template <class T>
class GraphNode{
public:
	GraphNode(int);
	~GraphNode();
	T* data;
	GraphNode<T>** nodes;
	void addNodes(int,GraphNode<T>**);
};

template <class T>
GraphNode<T>::GraphNode(int dt){
	data = new int {dt};
}

template <class T>
GraphNode<T>::~GraphNode(){
	delete data;
}

template <class T>
void GraphNode<T>::addNodes(int number, GraphNode<T>** arr){
	nodes = new GraphNode<T>*[number];
	for(int i=0; i<number; i++){
		nodes[i] = arr[i];
	}
}

template <class T>
int sizeOfArray(T* arr) {
	return sizeof(arr) / sizeof(arr[0]);
}

int createLl(GraphNode<int>* node, map<int, Stack<GraphNode<int>>*>* depthLists, int level = 0){
	if(node == NULL){
		return NULL_VALUE;
	}
	if((*depthLists)[level] == 0){
		(*depthLists)[level] = new Stack<GraphNode<int>>();
	}
	(*depthLists)[level]->push(node);
	GraphNode<int>* childNode;
	for(int i=0; i<size; i++){
		childNode = node->nodes[i];
		createLl(childNode, depthLists, level+1);
	}  
}

int main(){

	GraphNode<int>* root = new GraphNode<int>(2);
	GraphNode<int>* a = new GraphNode<int>(3);
	GraphNode<int>* b = new GraphNode<int>(4);
	GraphNode<int>* c = new GraphNode<int>(5);
	GraphNode<int>* d = new GraphNode<int>(6);
	GraphNode<int>* e = new GraphNode<int>(7);
	GraphNode<int>* f = new GraphNode<int>(8);
	GraphNode<int>* g = new GraphNode<int>(9);
	GraphNode<int>* h = new GraphNode<int>(10);
	GraphNode<int>* i = new GraphNode<int>(11);
	GraphNode<int>* j = new GraphNode<int>(12);
	GraphNode<int>* k = new GraphNode<int>(13);
	GraphNode<int>* arr1[4] = {a,b,c,d};
	root->addNodes(4, arr1);
	GraphNode<int>* arr2[3] = {e,f,g};
	b->addNodes(3, arr2);
	GraphNode<int>* arr3[2] = {h,i};
	c->addNodes(2, arr3);
	GraphNode<int>* arr4[2] = {j};
	i->addNodes(2, arr4);
	GraphNode<int>* arr5[1] = {k};
	j->addNodes(1, arr5);

	map<int, Stack<GraphNode<int>>*>* mainDepthLists = new map<int, Stack<GraphNode<int>>*>();
	createLl(root, mainDepthLists);
	cout << *(*mainDepthLists)[0]->peek()->data << endl;

	return 0; 
}
