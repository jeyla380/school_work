#include <iostream>
#include <vector>
#include <string>
#include <cstring>
using namespace std;

int main() {
   
   vector<string> inputStrings;
   vector<int> freq;
   
   int vecLength;
   int wordCount = 0;
   string currentWord = "";
   
   cin >> vecLength;
   //cout << numLength;
   
   inputStrings.resize(vecLength);
   freq.resize(vecLength);
   
   for(unsigned int i = 0; i < inputStrings.size(); i++)
   {
      cin >> inputStrings.at(i);
      //cout << inputStrings.at(i);
      
   }
   
   
   for (unsigned int i = 0; i < inputStrings.size(); i++)
   {
      wordCount = 0;
      currentWord = inputStrings.at(i);
      for (unsigned int j = 0; j < freq.size(); j++)
      {
         if(currentWord == inputStrings.at(j))
         {
            wordCount++;
         }
      }
      freq.at(i) = wordCount;
      cout << inputStrings.at(i) << " - " << freq.at(i) << endl;
   }
   
   

   return 0;
}
