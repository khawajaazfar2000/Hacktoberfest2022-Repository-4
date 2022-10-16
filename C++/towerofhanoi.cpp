#include<bits/stdc++.h>
using namespace std;
void towerofhanoi(int n,char src,char help, char dest){
    if(n==1){
        cout<<"Move disk 1 from "<<src<<" to "<<dest<<endl;
        return;
    }
    towerofhanoi(n-1,src,dest,help);
    cout<<"Move disk "<<n<<" from "<<src<<" to "<<dest<<endl;
    towerofhanoi(n-1,help,src,dest);
}
int main(){
    int n;
    cin>>n;
    towerofhanoi(n,'A','B','C');
    return 0;
}