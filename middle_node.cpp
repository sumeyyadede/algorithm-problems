#include <iostream>
#include <string>

using namespace std;

class Node{
public:
	Node(){
		next = NULL;
	}
	//void setValue(int value){
	//	data = value;
	//}
	//string getValue(){
	//	return data;
	//}
	string data;
	Node* next;
};

class LinkedList{
public:
	LinkedList(){
		head = NULL;
	}
	void printAll();
	void inserToFront(string);
	void insertToBack(string);
	Node* getHead(){
		return head;
	}
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
void LinkedList::insertToBack(string value){
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
void LinkedList::inserToFront(string value){
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

void middle_node(Node* node){
	node->data = node->next->data;
	node->next = node->next->next;
}

int main(){

	LinkedList list;
	list.insertToBack("a");
	list.inserToFront("b");
	list.inserToFront("c");
	list.inserToFront("d");
	list.inserToFront("e");
	list.inserToFront("f");
	list.printAll();
	cout<< endl << endl;
	Node* node = list.getHead()->next;
	middle_node(node);
	list.printAll();

	return 0;
}
