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
	void insert_head(int);
	void insert_front(int);
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
void LinkedList::insert_head(int value){
	Node* node = new Node;
	node->data = value;
	node->next = head;
	head = node;
}
void LinkedList::insert_front(int value){
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
	cout << "-----" << endl;
}

LinkedList* sum_lists(LinkedList* l1,LinkedList* l2){
	LinkedList* l3 = new LinkedList;
	Node* p_node = l1->getHead();
	Node* p_temp = l2->getHead(); 
	int remainder = 0;
	int x, y, z;
	while (p_node != NULL || p_temp != NULL){
		if (p_node != NULL){
			x = p_node->data;
			p_node = p_node->next;
		}
		else{
			x = 0;
		}
		if (p_temp != NULL){
			y = p_temp->data;
			p_temp = p_temp->next;
		}
		else{
			y = 0;
		}
		z = x + y + remainder;
		remainder = z / 10;
		l3->insert_front(z % 10);
	}
	if(remainder == 1){
		l3->insert_front(1);
	}
	return l3;
}

int main(){

	LinkedList* l1 = new LinkedList;
	l1->insert_head(1);
	l1->insert_head(9);
	l1->insert_head(2);
	l1->insert_head(2);
	l1->insert_head(2);
	l1->insert_head(2);
	l1->printAll();
	LinkedList* l2 = new LinkedList;
	l2->insert_head(6);
	l2->insert_head(4);
	l2->insert_head(3);
	l2->printAll();
	LinkedList* l3 = sum_lists(l1,l2);
	l3->printAll();

	return 0;
}
