#include <iostream>
#include <string>
using namespace std;

#include "roster.h"



Roster::Roster() //constructor
{
	studentID = "N/A";
	firstName = "N/A";
	lastName = "N/A";
	emailAddress = "N/A";
	age = 0;
	daysInCourse1 = 0;
	daysInCourse2 = 0;
	daysInCourse3 = 0;
	degreeProgram;
}

Roster::~Roster()
{
	for (int i = 0; i < 5; i++)
	{
		//this will deconstruct the classRosterArray and delete the allocated memory
		delete classRosterArray[i];
	}
}


DegreeProgram convert(const string& str) //this function converts the string into a readable format for DegreeProgram enum
{
	if (str == "SECURITY")
	{
		return SECURITY;
	}
	else if (str == "NETWORK")
	{
		return NETWORK;
	}
	else
	{
		return SOFTWARE;
	}
}

//this will parse the data and set the data into each section of Student::Student()
void Roster::ParseData(const string *array)
{
	const string *arrayPtr = array;
	for (int i = 0; i < 5; i++)
	{
		size_t x = arrayPtr[i].find(","); //returns the index of where the first "," is: 2
		studentObj[i].SetStudentId(arrayPtr[i].substr(0, x)); //this finds the substring from 0 and look for length in x (2). Assigns it to the studentId

		size_t y = x + 1; //this will create 2 + 1 which is the index of 3 for the first sting of data (J in John)
		x = arrayPtr[i].find(",", y); //this will start at index 3 to look for the next "," which is index 7 (John) for the first string of data
		studentObj[i].SetFirstName(arrayPtr[i].substr(y, x - y)); //this finds the substring from 3 and is 7 - 3 = 4 in length

		y = x + 1; //7 + 1 = index 8 (S in Smith)
		x = arrayPtr[i].find(",", y); //start at index 8 to look for the next ","
		studentObj[i].SetLastName(arrayPtr[i].substr(y, x - y)); //finds the substring from 8 to the end of word before ","

		y = x + 1;
		x = arrayPtr[i].find(",", y);
		studentObj[i].SetEmail(arrayPtr[i].substr(y, x - y));

		y = x + 1;
		x = arrayPtr[i].find(",", y);
		string str = arrayPtr[i].substr(y, x - y); //this is the int for age, but in a string
		int num = stoi(str); //this converts the string into an int
		studentObj[i].SetAge(num);

		y = x + 1;
		x = arrayPtr[i].find(",", y);
		int courseDay1 = stoi(arrayPtr[i].substr(y, x - y)); //puts the int into a variable to put into the .SetNumberOfDays later
		studentObj[i].SetCourseDays1(courseDay1);
		y = x + 1;
		x = arrayPtr[i].find(",", y);
		int courseDay2 = stoi(arrayPtr[i].substr(y, x - y)); //puts the int into a variable to put into the .SetNumberOfDays later
		studentObj[i].SetCourseDays2(courseDay2);
		y = x + 1;
		x = arrayPtr[i].find(",", y);
		int courseDay3 = stoi(arrayPtr[i].substr(y, x - y)); //puts the int into a variable to put into the .SetNumberOfDays later
		studentObj[i].SetCourseDays3(courseDay3);

		y = x + 1;
		x = arrayPtr[i].find(",", y);
		string convertStr = arrayPtr[i].substr(y, x - y);
		DegreeProgram program = convert(convertStr); //declares the program variable as a converted string to input into .SetDegreeProgram()
		studentObj[i].SetDegreeProgram(program);


		add(studentObj[i].getStudentId(), studentObj[i].getFirstName(), studentObj[i].getLastName(), studentObj[i].getEmail(), studentObj[i].getAge(), studentObj[i].getCourseDays1(), studentObj[i].getCourseDays2(), studentObj[i].getCourseDays3(), studentObj[i].getDegreeProgram());
	}

}

//this adds the data from ParseData() and puts it into a new Student class each time, which populates classRosterArray
void Roster::add(string studentID, string firstName, string lastName, string emailAddress, int age, int daysInCourse1, int daysInCourse2, int daysInCourse3, DegreeProgram degreeprogram)
{
	//each time the a new Student is added, the classRosterArray goes up one
	classRosterArray[index++] = new Student(studentID, firstName, lastName, emailAddress, age, daysInCourse1, daysInCourse2, daysInCourse3, degreeprogram);
}


void Roster::remove(string studentID)
{	
	int removeIndex = 0;
	for (int i = 0; i < 5; i++) //going to shift the elements of classRosterArray and remove the last element
	{
		if (studentID == classRosterArray[i]->getStudentId()) //looks for the studentID and compares it to the classRosterArray
		{
			removeIndex = i;
		}
	}

	if (studentID == classRosterArray[removeIndex]->getStudentId())
	{
		//cout << removeIndex << endl;
		int sizeOfArray = 5;
		for (int i = removeIndex; i < sizeOfArray - 1; i++) //5 is the size of the studentData array, and we are going to shorten it by 1 to remove the element we are looking for.
		{
			//classRosterArray[1] = classRosterArray[2]
			classRosterArray[i] = classRosterArray[i + 1];
		}
		classRosterArray[index--];
	}
	else
	{
		cout << endl;
		cout << "Student ID: " << studentID << " is not available." << endl;
	}

}


//this takes the Print() function from Student and implements the classRosterArray to it
void Roster::printAll()
{	
	cout << "Print Out All Students: " << endl;
	for (int i = 0; i < Roster::index; i++)
	{
		classRosterArray[i]->Print();
	}
	cout << endl;
}


//loop through all the studentIDs or just the one in the parameter?
void Roster::printAverageDaysInCourse(string studentID)
{
	int numIndex = 0;
	for (int i = 0; i < 5; i++) //going to shift the elements of classRosterArray and remove the last element
	{
		if (studentID == classRosterArray[i]->getStudentId()) //looks for the studentID and compares it to the classRosterArray
		{
			numIndex = i;
		}
	}
	
	int totalDays = classRosterArray[numIndex]->getCourseDays1() + classRosterArray[numIndex]->getCourseDays2() + classRosterArray[numIndex]->getCourseDays3();
	int averageDays = totalDays / 3;

	cout << "Average Day In Course: " << endl;
	cout << "Student ID: " << studentID << ", Average Days in Course: " << averageDays << endl;
	cout << endl;
}


//verifies correct emails (by not printing them) and prints out invalid ones
void Roster::printInvalidEmails()
{
	cout << "Print Out All Invalid Emails: " << endl;
	
	string validEmail = "";

	//valid email will have '@', '.', and no space
	for (int i = 0; i < 5; i++)
	{
		//looks for emails that have '@', emails that have '.', and emails that don't have a space
		if (classRosterArray[i]->getEmail().find('@') != string::npos && classRosterArray[i]->getEmail().find('.') != string::npos && classRosterArray[i]->getEmail().find(" ") == string::npos)
		{
			//cout << classRosterArray[i]->getEmail() << endl;
			validEmail = classRosterArray[i]->getEmail();
		}
		else
		{
			cout << classRosterArray[i]->getEmail() << " - INVALID" << endl;
		}
	}
	cout << endl;
}


void Roster::printByDegreeProgram(DegreeProgram degreeprogram)
{
	cout << "Print Out By Degree Program: " << endl;

	for (int i = 0; i < 5; i++)
	{
		if (classRosterArray[i]->getDegreeProgram() == degreeprogram)
		{
			cout << classRosterArray[i]->getStudentId() << '\t';
			cout << classRosterArray[i]->getFirstName() << '\t';
			cout << classRosterArray[i]->getLastName() << '\t';
			cout << classRosterArray[i]->getAge() << '\t';
			cout << "{" << classRosterArray[i]->getCourseDays1() << ", " << classRosterArray[i]->getCourseDays2() << ", " << classRosterArray[i]->getCourseDays3() << "}\t";

			//this turns the values of the enum and turns them into strings
			const char* type[] = { "Security", "Network", "Software" };
			string degreeType;
			if (classRosterArray[i]->getDegreeProgram() == 0)
			{
				degreeType = type[SECURITY];
			}
			else if (classRosterArray[i]->getDegreeProgram() == 1)
			{
				degreeType = type[NETWORK];
			}
			else
			{
				degreeType = type[SOFTWARE];
			}
			cout << degreeType << endl;
		}
	}
	cout << endl;
}
