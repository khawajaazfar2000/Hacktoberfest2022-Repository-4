#include<iostream>
using namespace std;
class Node{
	public:
		int data;
		Node* next;
};
void display(Node*p){
	if(p!=NULL){
		cout<< p->data<<endl;
		display(p->next);
	}
}
int main(){
	Node* First = NULL;
	Node* second = NULL;
	Node* third = NULL;
	Node* forth = NULL;
	
	
	 First = new Node();
	 second = new Node();
	 third = new Node();
	 forth = new Node();
	 
	 First -> data = 43;
	 First->next = second;
	 
	 second -> data = 23;
	 second->next = third;
	 
	 third -> data = 987;
	 third->next = forth;
	 
	 forth -> data = 78;
	 forth->next = NULL;
	 
	 display(First);
	 return 0;
}

