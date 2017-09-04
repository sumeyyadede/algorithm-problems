#include <iostream>
#include <cstdlib>

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

Node<int>* createBstOptimized(int* arr, int start = NULL_VALUE, int end = NULL_VALUE){
	// if(start == NULL_VALUE){
	// 	start = 0;
	// 	end = (sizeof(arr) / sizeof(int*)) -1;
	// 	cout << "end" << endl;
	// 	cout << sizeof(arr) << endl;
	// }
	if(start > end){
		return NULL;
	}
	int m = (start + end)/2;
	Node<int>* n = new Node<int>();
	n->data = arr[m];
	n->left = createBstOptimized(arr, start, m-1);
	n->right = createBstOptimized(arr, m+1, end);
	return n;
}

int preOrder(Node<int>* n){
	if(!n){
		return NULL_VALUE;
	}
	cout << n->data << endl;
	preOrder(n->left);
	preOrder(n->right);
}

int main(){

	int arr[10];
	for(int i=0; i < 10; i++){
		int random_integer = rand()%1000;
		arr[i] = random_integer;
		cout << arr[i] << endl;
	}

	int temp;
	for(int i=0;i< 10;i++){
		for(int j=0;j< 10-i;j++){
			if(arr[j]>arr[j+1]){
				temp=arr[j];				
				arr[j]=arr[j+1];
				arr[j+1]=temp;
			}
		}
	}
	
	cout << "sorted" << endl;
	for(int i=0; i < 10; i++){
		cout << arr[i] << endl;
	}

	Node<int>* n;
	n = createBstOptimized(arr, 0, 10);
	cout << "preOrder" << endl;
	preOrder(n);

	return 0;
}
