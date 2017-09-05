#include <iostream>

using namespace std;

#define NULL_VALUE -1

template <class T>
class Node{
public:
	Node();
	~Node();
	T data;
	Node<T>* left;
	Node<T>* right;
	Node<T>* parent;			
};

template <class T>
Node<T>::Node(){
	left = NULL;
	right = NULL;
	parent = NULL;
}

template <class T>
Node<T>::~Node(){
	delete data;
}

int inOrderSuccessor(Node<int>* node){
	if(node == NULL){
		return NULL_VALUE;
	}
	Node<int>* n;
	Node<int>* c;
	if(node->right){
		n = node->right;
		while(n->left != NULL){
			n = n->left;
		}
		return n->data;
	}
	else if(node->parent){
		n = node->parent;
		c = node;
		while(n != NULL && n->left != c){
			c = n;
			n = n->parent;
		}
		return n->data;
	}
	return NULL_VALUE;
}

int main(){

	Node<int>* root = new Node<int>();
	root->data = 15;
	Node<int>* a = new Node<int>();
	a->data = 8;
	Node<int>* b = new Node<int>();
	b->data = 20;
	Node<int>* c = new Node<int>();
	c->data = 5;
	Node<int>* d = new Node<int>();
	d->data = 10;
	Node<int>* e = new Node<int>();
	e->data = 16;
	Node<int>* f = new Node<int>();
	f->data = 30;
	Node<int>* g = new Node<int>();
	g->data = 9;
	Node<int>* h = new Node<int>();
	h->data = 12;
	root->left = a;
	root->left->parent = root;
	root->right = b;
	root->right->parent = root;
	root->right->left = e;
	root->right->left->parent = root->right;	
	root->right->right = f;
	root->left->left = c;
	root->left->left->parent = root->left;
	root->left->right = d;
	root->left->right->parent = root->left;
	root->left->right->left = g;
	root->left->right->left->parent = root->left->right;
	root->left->right->right = h;
	root->left->right->right->parent = root->left->right;

	cout << inOrderSuccessor(root->left->left) << endl;

	return 0;
}
