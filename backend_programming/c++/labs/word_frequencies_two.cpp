#include <iostream>
#include <vector> 
#include <string>
#include <cctype>
using namespace std;

//function that changes the string into lower case
void StrToLower(string& wordChange)
{
   for(unsigned int i = 0; i < wordChange.length(); i++)
   {
      wordChange[i] = tolower(wordChange[i]);
   }
}


int GetWordFrequency(vector<string> wordsList, string currWord)
{
   int wordCount = 0;
   
   for(unsigned int i = 0; i < wordsList.size(); i++)
   {
      wordCount = 0;
      StrToLower(currWord);
      
      for(unsigned int j = 0; j < wordsList.size(); j++)
      {
         StrToLower(wordsList.at(j));
         if(currWord == wordsList.at(j))
         {
            wordCount++;
         }
      }
   }
   return wordCount;
}

int main() {
   int inputNum;
   vector<string> inputList;
   
   cin >> inputNum;
   inputList.resize(inputNum);
   for(unsigned int i = 0; i < inputList.size(); i++)
   {
      cin >> inputList.at(i);
      //cout << inputList.at(i) << endl;
   }
   
   //needs to be separate from the first for loop since we need all the input put in first, and then go through the function after
   for(unsigned int i = 0; i < inputList.size(); i++)
   {
      cout << inputList.at(i) << " " << GetWordFrequency(inputList, inputList.at(i)) << endl;   
   }

   return 0;
}
