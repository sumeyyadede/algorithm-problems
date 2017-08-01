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
//private:
	char data;
	Node* next;
};

Node* loop_detection(Node* node){
	Node* fr = node->next->next;
	Node* sr = node->next;
	
	while(fr != sr){
		fr = fr->next->next;
		sr = sr->next;
	}

	sr = node;
	while(fr != sr){
		fr = fr->next;
		sr = sr->next;
	}

	return sr;
}

int main(){

	Node* node = new Node;
	node->data = 'A';
	node->next = new Node;
	node->next->data = 'B';
	node->next->next = new Node;
	node->next->next->data = 'C';
	node->next->next->next = new Node;
	node->next->next->next->data = 'D';
	node->next->next->next->next = new Node;
	node->next->next->next->next->data = 'E';
	node->next->next->next->next->next = new Node;
	node->next->next->next->next->next->data = 'F';
	node->next->next->next->next->next->next = node->next->next->next;

	Node* temp = loop_detection(node);
	cout << temp->data << endl;

	return 0;
}
