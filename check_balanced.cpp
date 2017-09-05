#include <iostream>

using namespace std;

template <class T>
class Node{
public:
	Node();
	~Node();
	T data;
	Node<T>* left;
	Node<T>* right;
};

template <class T>
Node<T>::Node(){
	left = NULL;
	right = NULL;
}

template <class T>
Node<T>::~Node(){
	delete data;
}

int checkBalanced(Node<int>* node){
	if(!node){
		return 0;
	}
	int left = checkBalanced(node->left);
	if(left == -1){
		return -1;
	}
	int right = checkBalanced(node->right);
	if(right == -1){
		return -1;
	}
	if(abs(left - right) > 1){
		return -1;
	}
	return max(left, right) + 1;
}

int main(){

	Node<int>* root = new Node<int>();
	root->data = 2;
	Node<int>* a = new Node<int>();
	a->data = 3;
	Node<int>* b = new Node<int>();
	b->data = 4;
	Node<int>* c = new Node<int>();
	c->data = 5;
	Node<int>* d = new Node<int>();
	d->data = 6;
	Node<int>* e = new Node<int>();
	e->data = 7;
	Node<int>* f = new Node<int>();
	f->data = 8;
	Node<int>* g = new Node<int>();
	g->data = 9;
	root->left = a;
	root->right = b;
	a->left = c;	
	a->right = e;	
	a->left->left = g;
	b->left = f;
	b->right = d;

	cout << checkBalanced(root) << endl;

	return 0;
}
