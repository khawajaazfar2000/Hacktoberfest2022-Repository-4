/* Given a reference (pointer to pointer)
to the head of a list and an int,
inserts a new node on the front of the list. */
#include <iostream>
using namespace std;
class Node {
public:
	int data;
	Node* next;
};
	void push(Node*n){
		// allocate node 
		while(n!= NULL){
                  cout<<n->data<<endl;
	          n = n->next;
		}
		
	}

int main(){
	Node* head = NULL;
	Node* second = NULL;
	
	head = new Node();
	second = new Node();

	head->data = 1; // assign data in first node
	head->next = second;
	
	second->data=3;
	second->next = NULL;
	push(head);
	return 0;
}
