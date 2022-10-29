#include <iostream>  

using namespace std;  

int main()  
{  
  //we initialize the factorial wih the value of 1 
   int i,fact=1,number;    
  cout<<"Enter any Number: ";    
 cin>>number;    
  for(i=1;i<=number;i++){   
      //At each iteration  we multiply the last value of the fact with the vlaue of i
      // when the condition in 'for' statement is satisfied, the value of factorial is gained
      fact=fact*i;  

  }    

  cout<<"Factorial of " <<number<<" is: "<<fact<<endl;  
  return 0;  

}  
