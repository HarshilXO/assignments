#include <iostream>
using namespace std;

int main()
{
    int a[100], t = -1, b;
    int d;
    cout << "push(1) or pop(0)" << endl;
    cin >> d;

    if (d == 1)
    {
    up:
        char c = 0;
        cout << "Enter integer value to be pushed: ";
        cin >> b;

        if (t < 99)
        {
            a[t + 1] = b;
            t++;
            cout << b << "Pushed Successfully";
        }
        else
        {
            cout << "Stack is Overflown";
        }
        cout << "\nDo you want to continue to push elements?(Y/N): ";
        cin >> c;
        if (c == 'Y' || c == 'y')
        {
            goto up;
        }
        else
        {
            goto down;
        }
    }
    else
    {
    down:
        char f;
        cout << "want to pop?(Y/N)";
        cin >> f;
        if (f == 'y')
        {
        repop:
            if (t < -1)
            {
                cout << "stack is underflown" << endl;
            }
            else
            {
                t--;
                cout << "popped successfully" << endl;
            }
        }
    }
    cout << "The Stack is: ";
    for (int i = 0; i < t + 1; i++)
    {
        cout << " " << a[i];
    }
    char g;
    cout << "\nwant to repop?(Y/N)";
    cin >> g;
    if (g == 'y')
    {
        goto repop;
    }
    else
    {
        cout << "The Stack is: ";
        for (int i = 0; i < t + 1; i++)
        {
            cout << " " << a[i];
        }
    }
    return 0;
}