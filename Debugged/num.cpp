#include<iostream>
using namespace std;

int numOfDigits(int n, int count = 1)
{
    if(n > 9)
    {
        count++;
        numOfDigits(n/10, count);
    }

    return count;
}

int main()
{
    
    cout << numOfDigits(3545445) << endl;

    return 0;
}