#include <iostream>
using namespace std;

int main() {

    int money;

    int dollars = 100;
    int quarters = 25;
    int dimes = 10;
    int nickels = 5;

    int dollarAmount;
    int quarterAmount;
    int dimeAmount;
    int nickelAmount;

    int dollarLeftover;
    int quarterLeftover;
    int dimeLeftover;
    int nickelLeftover;

    cin >> money;



    if (money)
    {
        //DOLLARS
        dollarAmount = money / dollars; //this will group the dollars together
        dollarLeftover = money % dollars; //this will find the remainders that can't be grouped by 100s
        if (dollarAmount > 0)
        {
            if (dollarAmount > 1)
            {
                cout << dollarAmount << " Dollars" << endl;
            }
            else
            {
                cout << dollarAmount << " Dollar" << endl;
            }
        }

        //QUARTERS
        quarterAmount = dollarLeftover / quarters; //this will group the quarters together
        quarterLeftover = dollarLeftover % quarters; //this will find the remainders that can't be grouped by 25s
        if (quarterAmount > 0)
        {
            if (quarterAmount > 1)
            {
                cout << quarterAmount << " Quarters" << endl;
            }
            else
            {
                cout << quarterAmount << " Quarter" << endl;
            }
        }


        //DIMES
        dimeAmount = quarterLeftover / dimes; //this will group dimes together
        dimeLeftover = quarterLeftover % dimes; //this will find the remainders that can't be grouped by 10s
        if (dimeAmount > 0)
        {
            if (dimeAmount > 1)
            {
                cout << dimeAmount << " Dimes" << endl;
            }
            else
            {
                cout << dimeAmount << " Dime" << endl;
            }
        }


        //NICKELS
        nickelAmount = dimeLeftover / nickels; //this will group nickels together
        nickelLeftover = dimeLeftover % nickels; //this will find the remainders that can't be grouped by 5s
        if (nickelAmount > 0)
        {
            if (nickelAmount > 1)
            {
                cout << nickelAmount << " Nickels" << endl;
            }
            else
            {
                cout << nickelAmount << " Nickel" << endl;
            }
        }


        //PENNIES
        if (nickelLeftover > 0)
        {
            if (nickelLeftover > 1)
            {
                cout << nickelLeftover << " Pennies" << endl;
            }
            else
            {
                cout << nickelLeftover << " Penny" << endl;
            }
        }
    }
    else if (money == 0)
    {
        cout << "No change" << endl;
    }

    return 0;
}
