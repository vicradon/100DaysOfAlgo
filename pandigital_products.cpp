#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool isPandigital(int multiplier, int multiplicand){
    int fullSet[9];
    for (int i = 0; i < 9; i++){
        fullSet[i] = i+1;
    };

    string strigifiedMultiplier = to_string(multiplier);
    string strigifiedMultiplicand = to_string(multiplicand);
    string strigifiedProduct = to_string(multiplier * multiplicand);

    string concatenated = strigifiedMultiplier + strigifiedMultiplicand + strigifiedProduct;
    sort(concatenated.begin(), concatenated.end());

    
    for (int i = 0; i < 9; i++) cout << fullSet[i];
    cout << endl;
    cout << concatenated << "\n";

    for (int i = 0; i < 9; i++){
        if (concatenated[i] != fullSet[i]){
            cout << concatenated[i]  << "\n";
            cout << fullSet[i]  << "\n";
            return false;
        }
        if (concatenated[i] == fullSet[i]){
            cout << concatenated[i]  << "\n";
            cout << fullSet[i]  << "\n";
        }
    }
    return true;
}

int main()
{
    cout << isPandigital(39, 186) << "\n";

    return 0;
}