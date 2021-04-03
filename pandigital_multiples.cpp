#include <iostream>
#include <cstdio>
#include <vector>
#include <bits/stdc++.h>
using namespace std;

bool isPandigital(int number, int concat_set[])
{
    return false;
}

int *vectToArray(vector<int> vect)
{
    int arr_size = vect.size();
    int arr[arr_size];
    for (int i = 0; i < arr_size; i++)
    {
        arr[i] = vect.at(i);
    }
    return arr;
}

int main()
{

    int maxPandigital;

    vector<vector<int>> concat_sets;
    for (int index = 1; index <= 9; index++)
    {
        vector<int> subVect;
        for (int jindex = 1; jindex <= index; jindex++)
        {
            subVect.push_back(jindex);
        }
        concat_sets.push_back(subVect);
    }

    // for (auto index = concat_sets.begin(); index != concat_sets.end(); ++index)
    //     cout << index << endl;

    cout << concat_sets.at(4).at(3) << endl;

    for (int num = 0; num < 100000000; num++)
    {
        for (int index = 0; index < 9; index++)
        {
            int *concat_set = vectToArray(concat_sets.at(index));
            if (isPandigital(num, concat_set))
            {
                if (maxPandigital < num)
                {
                    maxPandigital = num;
                }
            }
        }
    }

    return maxPandigital;
}
