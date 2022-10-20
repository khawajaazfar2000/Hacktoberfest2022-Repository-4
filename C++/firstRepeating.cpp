# include <iostream>
using namespace std ;
void firstRepeating(int arr[],int s){
	for(int i=0;i<s;i++){
		int temp=arr[i];
		for(int j=i+1;j<s;j++){
			if(temp!=arr[j]){
				
							

			}
			else{
				cout<<i+1;
				break;
			}
		}
		
	}
}
int main(){
	int arr[]={1, 5, 3, 4, 3, 5, 6};
	int s=7;
	firstRepeating(arr,s);
	
}
