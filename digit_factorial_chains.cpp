#include <iostream>
#include <string>
using namespace std;

int factorialSum(int number)
{
    string num_str = to_string(number);
    long factorials[10] = {1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880};
    long sum = 0;

    for (int i = 0; i < num_str.length(); i++)
    {
        cout << num_str[i] << "\n";
        sum += factorials[num_str[i]];
    }

    return sum;
}

int main()
{
    cout << factorialSum(169) << endl;
    return 0;
}