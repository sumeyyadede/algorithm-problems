#include <iostream>

using namespace std;

class Node{
public:
	Node(){
		next = NULL;
	}
	int data;
	Node* next;
};

Node* ll_intersection(Node* p_node1,Node* p_node2){
	Node* p_temp1 = p_node1;
	Node* p_temp2 = p_node2;
	int len1 = 0 , len2 = 0;
	int diff;
	
	while(p_temp1 != NULL || p_temp2 != NULL){
		if(p_temp1 != NULL){
			len1 += 1;
			p_temp1 = p_temp1->next;
		}
		if(p_temp2 != NULL){
			len2 += 1;
			p_temp2 = p_temp2->next;
		}
	}

	diff = abs(len2 - len1);
	for(int i=0; i<diff; i++){
		if(len2 > len1){
			p_node2 = p_node2->next;
		}
		else{
			p_node1 = p_node1->next;
		}
	}


	while(p_node2 != NULL){
		if(p_node1 == p_node2){
			return p_node1;
		}
		p_node1 = p_node1->next;
		p_node2 = p_node2->next;
	}
 }

int main(){
	Node* p_node1 = new Node;
	p_node1->data = 5;
	p_node1->next = new Node;
	p_node1->next->data = 6;
	p_node1->next->next = new Node;
	p_node1->next->next->data = 7;
    p_node1->next->next->next = new Node;
	p_node1->next->next->next->data = 8;
    p_node1->next->next->next->next = new Node;
	p_node1->next->next->next->next->data = 3;
	p_node1->next->next->next->next->next = NULL;
	Node* p_node2 = new Node;
	p_node2->data = 3;
	p_node2->next = new Node;
	p_node2->next->data = 5;
	p_node2->next->next = new Node;
	p_node2->next->next->data = 9;
	p_node2->next->next->next = new Node;
	p_node2->next->next->next->next = p_node1->next->next;

	Node* p_node3 = ll_intersection(p_node1,p_node2);
	while(p_node3 != NULL){
		cout << p_node3->data << endl;
		p_node3 = p_node3->next;
	}	
	return 0;
}
