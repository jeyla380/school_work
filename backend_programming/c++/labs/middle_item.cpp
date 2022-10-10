#include <iostream>
#include <vector>   // Must include vector library to use vectors
using namespace std;

int main() {

   vector<int> multipleNum(100);
   
   int numInput;
   int middleIndex;
   int count = 0;
   
   //FINDS THE LENGTH OF THE VECTOR, RESIZES BASED ON INPUT
   for (unsigned int i = 0; i < multipleNum.size(); i++)
   {
      cin >> numInput;
      multipleNum.at(i) = numInput;
      
      if (multipleNum.at(i) < 0)
      {
         break;   
      }
      else
      { 
         count++; 
      }
   }
   
   
   multipleNum.resize(count);
   if (multipleNum.size() > 9)
   {
      cout << "Too many numbers" << endl;   
   }   
   else
   {
      //MIDDLE NUMBER
      //cout << count;
      middleIndex = (multipleNum.size() - 1) / 2;
      cout << "Middle item: " << multipleNum.at(middleIndex) << endl;   
   }

   return 0;
}
