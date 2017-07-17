#include <iostream>
#include <map>
#include <cassert>

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
	void findDuplicates();

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

void LinkedList::findDuplicates(){

	Node* node = new Node;
	node = head;
	Node* prev_node = new Node;
	prev_node = NULL;

	map<int, int> ht;
	
	while(node->next != NULL){
		if(ht[node->data] == 0){
			ht[node->data] = 1;
			prev_node = node;
		}
		else{
			prev_node->next = node->next;
		}
		node = node->next;
	}
}

int main(){

	LinkedList list;
	list.insertToBack(1);
	list.insertToBack(2);
	list.inserToFront(3);
	list.inserToFront(3);
	list.inserToFront(4);
	list.inserToFront(5);
	list.inserToFront(6);
	list.inserToFront(4);
	list.inserToFront(3);
	list.inserToFront(9);
	list.inserToFront(15);
	list.printAll();
	cout<< endl << endl;
	list.findDuplicates();
	list.printAll();

	return 0;
}
