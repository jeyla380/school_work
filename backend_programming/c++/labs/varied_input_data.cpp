#include <iostream>
#include <iomanip>
using namespace std;

int main() {

    int currentNum;
    int maxNum = 0;
    double totalSum = 0;
    double avgNum;
    int inputValue;
    int count = 0;

    while (inputValue >= 0)
    {
        cin >> inputValue;
        //cout << inputValue;

        if (inputValue > -1)
        {

            currentNum = inputValue;

            //MAX NUM
            if (maxNum == 0)
            {
                maxNum = currentNum;
            }
            else if (currentNum > maxNum)
            {
                maxNum = currentNum;
                //cout << maxNum;
            }

            //AVG
            if (maxNum >= 0)
            {
                totalSum = totalSum + currentNum;
                count++;
            }
        }
    }
    //cout << totalSum << " "; 
    avgNum = totalSum / count;

    cout << fixed << setprecision(2);
    cout << maxNum << " " << avgNum << endl;

    return 0;
}
