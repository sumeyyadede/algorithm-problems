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

int lastItem = -1;
bool validateBstLast(Node<int>* node){
	if(node == NULL){
		return true;
	}
	if(!validateBstLast(node->left)){
		return false;
	}
	if(lastItem == -1){
		lastItem = node->data;
	}
	else if(lastItem > node->data){
		return false;
	}
	else{
		lastItem = node->data;
	}
	if(!validateBstLast(node->right)){
		return false;
	}
	return true;
}

bool validateBstMinMax(Node<int>* node, int mi = -1, int ma = -1){
	if(node == NULL){
		return true;
	}
	if((mi != -1 && mi > node->data) || (ma != -1 && ma < node->data) \
		|| (!validateBstMinMax(node->left, mi, node->data))\
		|| (!validateBstMinMax(node->right, node->data, ma))){
		return false;
	}
	return true;
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
	g->data = 7;
	root->left = a;
	root->right = b;
	root->right->left = e;	
	root->right->right = f;
	root->left->left = c;
	root->left->right = d;
	root->left->right->left = g;

	cout << validateBstLast(root) << endl;
	cout << validateBstMinMax(root) << endl;

	return 0;
}
