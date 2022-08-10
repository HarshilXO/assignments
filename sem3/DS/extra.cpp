#include <iostream>
using namespace std;

int main()
{
	int i, a, arr[5], s;
	cout << "enter elements of array: " << endl;
	cin >> a;
	
	cout << "enter: " << a << " numbers \n";
	
	for (i = 0; i < a; i++)
	{
		cin >> arr[i];
	}
	cout << "The array is: " << endl;
	
	for (i = 0; i < a; i++)
	{
		cout << arr[i] << endl;
	}
	
	cout << "enter number to search: ";
	cin >> s;

    for (i = 0; i < a; i++)
    {	
        if(arr[i] == s)
        {
            cout << "element found at index: " << i;
            break;
        }
    }
    if(arr[i] != s)
    {
        cout << "not found.";
    }
	return 0;
}