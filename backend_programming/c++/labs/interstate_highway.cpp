#include <iostream>
using namespace std;

int main() {
    int highwayNumber;
    int usHighwayNum;
    int auxHighwayNum;

    cin >> highwayNumber;

    //U.S. interstate highways = 1 - 99
    //Auxiliary highways = 100 - 999 (100, 200, 300, 400, etc. is not valid)
    // Odd numbers go north/south, even numbers go east/west

    /*service the primary highway indicated by the rightmost two digits.
    I-405 services I-5, and I-290 services I-90*/

    //even highway numbers
    if (highwayNumber % 2 == 0)
    {
        //U.S. interstate highways 1 - 99
        if (highwayNumber > 0 && highwayNumber < 100)
        {
            //100, 200, 300, 400, etc. is not valid
            if (highwayNumber % 100 == 0)
            {
                cout << highwayNumber << " is not a valid interstate highway number." << endl;
            }
            //if the number is valid (not the one above), it will print out properly
            else
            {
                usHighwayNum = highwayNumber;
                cout << "I-" << usHighwayNum << " is primary, going east/west." << endl;
            }

        }

        //Auxiliary highways = 100 - 999
        else if (highwayNumber > 100 && highwayNumber < 1000)
        {
            if (highwayNumber % 100 == 0)
            {
                cout << highwayNumber << " is not a valid interstate highway number." << endl;
            }

            else
            {
                auxHighwayNum = highwayNumber;
                usHighwayNum = highwayNumber % 100;
                cout << "I-" << auxHighwayNum << " is auxiliary, serving I-" << usHighwayNum << ", going east/west." << endl;
            }

        }

        //numbers less than 1, and more than 999
        else
        {
            cout << highwayNumber << " is not a valid interstate highway number." << endl;
        }
    }


    //odd highway numbers
    else
    {
        //U.S. interstate highways 1 - 99
        if (highwayNumber > 0 && highwayNumber < 100)
        {
            if (highwayNumber % 100 == 0)
            {
                cout << highwayNumber << " is not a valid interstate highway number." << endl;
            }

            else
            {
                usHighwayNum = highwayNumber;
                cout << "I-" << usHighwayNum << " is primary, going north/south." << endl;
            }
        }

        //Auxiliary highways = 100 - 999
        else if (highwayNumber > 100 && highwayNumber < 1000)
        {
            if (highwayNumber % 100 == 0)
            {
                cout << highwayNumber << " is not a valid interstate highway number." << endl;
            }

            else
            {
                auxHighwayNum = highwayNumber;
                usHighwayNum = highwayNumber % 100;
                cout << "I-" << auxHighwayNum << " is auxiliary, serving I-" << usHighwayNum << ", going north/south." << endl;
            }
        }

        else
        {
            cout << highwayNumber << " is not a valid interstate highway number." << endl;
        }
    }



    return 0;
}
