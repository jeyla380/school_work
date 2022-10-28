#include <iostream>
#include<string>

#ifndef ROSTERH
#define ROSTERH

#include "student.h"

class Roster
{
public:
	Roster(); //constructor
	~Roster(); //destructor
	void ParseData(const string *array);

	void add(string studentID, string firstName, string lastName, string emailAddress, int age, int daysInCourse1, int daysInCourse2, int daysInCourse3, DegreeProgram degreeprogram);
	void remove(string studentID);

	void printAll();
	void printAverageDaysInCourse(string studentID);
	void printInvalidEmails();
	void printByDegreeProgram(DegreeProgram degreeProgram);

	int index = 0;

	//array of pointers that will hold the data
	Student* classRosterArray[5]; //this is the length of data from studentData table
	Student* studentObj = new Student[5]; //student object that will hold each student

private:
	std::string studentID;
	std::string firstName;
	std::string lastName;
	std::string emailAddress;
	int age;
	int daysInCourse1;
	int daysInCourse2;
	int daysInCourse3;
	DegreeProgram degreeProgram;
};


#endif
