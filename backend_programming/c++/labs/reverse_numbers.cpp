#include <iostream>
#include <vector>   // Must include vector library to use vectors
using namespace std;

int main() {

    int numInput;
    int multipleNum;
    vector<int> userInts; // A vector to hold the user's input integers

    cin >> numInput;
    //cout << numInput;

    userInts.resize(numInput);
    for (unsigned int i = 0; i < userInts.size(); i++)
    {
        cin >> multipleNum;
        userInts.at(i) = multipleNum;
    }

    //cout << userInts[0];

    int j = userInts.size() - 1;
    while (j >= 0)
    {
        cout << userInts.at(j) << ",";
        j--;
    }
    cout << endl;


    return 0;
}
