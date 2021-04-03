#include <iostream>
using namespace std;

int main()
{
    int rangeMin = 1, rangeMax = 1000;

    int sumOfMultiples = 0;
    for (int index = rangeMin; index < rangeMax; index++)
    {
        if (index % 3 == 0 || index % 5 == 0)
        {
            sumOfMultiples += index;
        }
    }
    cout << sumOfMultiples << endl;
    return 0;
}
