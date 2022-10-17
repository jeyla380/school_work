#include <iostream>
#include <vector>
using namespace std;

void SortVector(vector<int>& myVec)
{
   for(unsigned int i = 0; i < myVec.size(); i++)
   {
      for(unsigned int j = i + 1; j < myVec.size(); j++)
      {
         int num = i;
         if(myVec.at(j) > myVec.at(num))
         {
            num = j;
         }
         int temp = myVec.at(num);
         myVec.at(num) = myVec.at(i);
         myVec.at(i) = temp;
      }
      cout << myVec.at(i) << ",";
   }
   cout << endl;
}

int main() {
   int inputNum;
   vector<int> inputValues;
   
   cin >> inputNum;
   
   inputValues.resize(inputNum);
   for(unsigned int i = 0; i < inputValues.size(); i++)
   {
      cin >> inputValues.at(i); 
      //cout << inputValues.at(i);
   }
   SortVector(inputValues);

   return 0;
}
