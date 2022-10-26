#include <bits/stdc++.h>
using namespace std;
bool isPrime(int n)
{
	if (n <= 1)
		return false;
	for (int i = 2; i <= sqrt(n); i++)
		if (n % i == 0)
			return false;

	return true;
}

int main()
{
	int number;
	cout<<"Enter the number to check: ">>endl;
	cin>>number;
	isPrime(number) ? cout << " true\n" : cout << " false\n";
	return 0;
}
