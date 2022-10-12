#include <iostream>
using namespace std;

int linearSearch(int n, int array[], int x) {
    for(int i=0;i<n;i++) if(array[i]==x) return i+1;
    return -1;
}

int main(void) {
  int array[] = {3, 4, 5, 6, 7, 8, 9};
  int x = 4;
  int n = sizeof(array) / sizeof(array[0]);
  int result = linearSearch(n, array, x);
  if (result == -1)
    printf("Not found");
  else
    printf("Element is found at index %d", result);
}
