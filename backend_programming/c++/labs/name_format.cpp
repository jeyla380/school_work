#include <iostream>
#include <string>
using namespace std;

int main() {

    string firstName, middleName, lastName, fullName;
    getline(cin, fullName);

    int firstSpace = fullName.find(" "); //this is the space after the first name
    //cout << firstSpace;
    firstName = fullName.substr(0, firstSpace);
    //cout << firstName;

    int secondSpace = fullName.find(" ", firstSpace + 1); //jumps to the next empty space (will be -1 if there's no other space)
    //cout << secondSpace; 
    if (secondSpace != -1)
    {
        middleName = fullName.substr(firstSpace + 1, (secondSpace - firstSpace) - 1);
        //cout << middleName;
        lastName = fullName.substr(secondSpace + 1, fullName.length() - 1);
        //cout << lastName;

        cout << lastName << ", " << firstName[0] << "." << middleName[0] << "." << endl;
    }
    else
    {
        lastName = fullName.substr(firstSpace + 1, fullName.length() - 1);
        //cout << lastName;

        cout << lastName << ", " << firstName[0] << "." << endl;
    }

    return 0;
}
