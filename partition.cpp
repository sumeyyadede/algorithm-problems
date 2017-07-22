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
	void setHead(Node*);
	Node* getHead();

private:
	Node* head;

};

void LinkedList::setHead(Node* node){
	this->head = node;
}
Node* LinkedList::getHead(){
	return this->head;
}
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

void partition(LinkedList* linked_list, int x){
	Node* node = linked_list->getHead();
	Node* prev_node = NULL;
	Node* head2 = NULL;
	Node* tail2 = NULL;

	while(node != NULL){
		if(((Node*) node)->data < x){
			if(head2 == NULL){
				head2 = node;
				tail2 = node;
				// cout << tail2->data<< endl;
			}
			else{
				((Node*) node)->next = (Node*) node;
				tail2 = node;
				// cout<< tail2->data<<endl;
			}
			if(prev_node == NULL){
				linked_list->setHead(((Node*) node)->next);
			}
			else{
				((Node*) prev_node)->next = ((Node*) node)->next;
			}
		}
		else{
			prev_node = node;
		}
		node = ((Node*) node)->next;
	}
    ((Node*) tail2)->next = linked_list->getHead();
	linked_list->setHead(((Node*)head2));
}

int main(){

	LinkedList* list = new LinkedList;
	list->insertToBack(1);
	list->insertToBack(9);
	list->inserToFront(2);
	list->inserToFront(6);
	list->inserToFront(4);
	list->inserToFront(3);
	list->inserToFront(8);
	list->inserToFront(9);
	list->printAll();
	cout<< endl << endl;
	partition(list,5);
	list->printAll();
	
	return 0;
}
