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
	void insert(int);
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
void LinkedList::insert(int value){
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
void LinkedList::printAll(){
	Node* p;
	p = head;
	while(p != NULL){
		cout << p->data << endl;
		p = p->next;
	}
}

void partition(LinkedList* linked_list, int x){
	Node* p_node = linked_list->getHead();
	Node* p_prev_node = NULL;
	Node* p_head2 = NULL;
	Node* p_tail2 = NULL;

	while(p_node != NULL){
		if(p_node->data < x){
			if(p_head2 == NULL){
				p_head2 = p_node;
				p_tail2 = p_node;
			}
			else{
				p_tail2->next = p_node;
				p_tail2 = p_node;
			}
			if(p_prev_node == NULL){
				linked_list->setHead(p_node->next);
			}
			else{
				p_prev_node->next = p_node->next;
			}
		}
		else{
			p_prev_node = p_node;
		}
		p_node = p_node->next;
	}
    p_tail2->next = linked_list->getHead();
	linked_list->setHead(p_head2);
}

int main(){

	LinkedList* list = new LinkedList;
	list->insert(1);
	list->insert(9);
	list->insert(2);
	list->insert(6);
	list->insert(4);
	list->insert(3);
	list->insert(8);
	list->insert(9);
	list->printAll();
	cout<< endl << endl;
	partition(list,5);
	list->printAll();
	
	return 0;
}
