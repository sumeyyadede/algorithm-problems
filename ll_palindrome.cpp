#include <iostream>
#include <map>

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
//private:
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

bool is_palindrome_ll(LinkedList* l1){
	Node* node = l1->getHead();
	int len = 0;
	map<int, int> ht;
	
	while(node != NULL){
		ht[node->data] = ht[node->data] + 1;
		node = node->next;
		len += 1;
	}
	int has_visit_odd = len % 2 == 0 ? 1 : 0;

	for(int i=0; i<ht.size(); i++){
		if(ht[i] % 2 == 1){
			if(has_visit_odd == 1){
				return false;
			}
			else{
				has_visit_odd = 1;
			}
		}	
	}
	return true;
}

int main(){

	LinkedList* l1 = new LinkedList;
	l1->insert_front(2);
	l1->insert_front(3);
	l1->insert_front(5);
	l1->insert_front(5); 
	l1->insert_front(3);
	l1->insert_front(2);
	l1->printAll();
	cout << is_palindrome_ll(l1) << endl;

	return 0;
}

