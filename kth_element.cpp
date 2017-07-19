#include <iostream>

using namespace std;

class Node{
public:
	Node(){
		next = NULL;
	}
	//void setValue(int value){
	//	data = value;
	//}
	//int getValue(){
	//	return data;
	//}
	int data;
	Node* next;
};

class LinkedList{

public:
	LinkedList(){
		head = NULL;
	}
	void printAll();
	void inserToFront(int);
	void insertToBack(int);
	int kthElement(int);

private:
	Node* head;

};

void LinkedList::printAll(){
	Node* p;
	p = head;
	while(p != NULL){
		cout << p->data << endl;
		p = p->next;
	}
}
void LinkedList::insertToBack(int value){
	Node* node = new Node;
	node->data = value;
	if(head == NULL){
		node->next = NULL;
	}
	else{
		node->next = head;
	}
	head = node;
}
void LinkedList::inserToFront(int value){
	Node* node = new Node;
	if(head == NULL){
		head = node;
	}
	else{
		Node* iter = head;
		while(iter->next != NULL){
			iter = iter->next;
		}
		iter->next = node;
	}
	node->data = value;
	node->next = NULL;
}
int LinkedList::kthElement(int counter){
	Node* node = new Node;
	node = head;
	Node* prev_node = new Node;
	prev_node = head;

	int i=0;
	/*while(node->next != NULL){
		if(i==(counter-1)){
			break;
		}
		node = node->next;
		i= i+1;
	}
	if(i != (counter-1)){
		cout << "not enough elements in list"<<endl;
		return -1;
	}
	*/
	for(int i=0; i<counter-1; i++){
		if(node->next != NULL){
			node = node->next;
		}
		else{
			cout<< "not enough elements in the list"<<endl;
			return -1;
		}
	}
	while(node->next != NULL){
		node = node->next;
		prev_node = prev_node->next;
	}
	return prev_node->data;
}

int main(){

	LinkedList list;
	list.insertToBack(1);
	list.insertToBack(2);
	list.inserToFront(3);
	list.inserToFront(3);
	list.inserToFront(4);
	//list.inserToFront(5);
	//list.inserToFront(6);
	//list.inserToFront(4);
	//list.inserToFront(3);
	//list.inserToFront(9);
	//list.inserToFront(15);
	list.printAll();
	cout<< endl;
	cout<< "return the 5th to last element: ";
	cout<< list.kthElement(5) << endl;

	return 0;
}
