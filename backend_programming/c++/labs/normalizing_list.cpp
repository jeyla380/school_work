#include <iostream>
#include <iomanip>
#include <vector>
using namespace std;

int main() {

   vector<double> multipleNums;
   double numList;
   double newList;
   int numLength;
   double maxNum;
   
   cin >> numLength;
   //cout << numLength;
   
   multipleNums.resize(numLength);
   for (unsigned int i = 0; i < multipleNums.size(); i++)
   {
      cin >> numList;
      //cout << numList;
      multipleNums.at(i) = numList;
      
      if (multipleNums.at(i) > maxNum)
      {
         maxNum = multipleNums.at(i);
      }
   }
   //cout << maxNum;
   
   for (unsigned int j = 0; j < multipleNums.size(); j++)
   {
      newList = double(multipleNums.at(j)) / maxNum;
      cout << fixed << setprecision(2);
      cout << newList << " ";
   }
   cout << endl;

   return 0;
}
