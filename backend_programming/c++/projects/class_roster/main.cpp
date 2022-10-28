#include <iostream>
#include <vector>
#include <string>
#include <cstring>
using namespace std;

#include "roster.h"





int main()
{
	cout << "C867 - Scripting and Programming: Appliations" << endl;
	cout << "Language: C++" << endl;
	cout << endl;
	cout << endl;
	
	
	const string studentData[] = { "A1,John,Smith,John1989@gm ail.com,20,30,35,40,SECURITY",
	"A2,Suzan,Erickson,Erickson_1990@gmailcom,19,50,30,40,NETWORK",
	"A3,Jack,Napoli,The_lawyer99yahoo.com,19,20,40,33,SOFTWARE",
	"A4,Erin,Black,Erin.black@comcast.net,22,50,58,40,SECURITY",
	"A5,[firstname],[lastname],[email],18,27,54,32,SOFTWARE" };

	/*
	//Test for student.h and student.cpp to ensure it works
	Student student1;

	student1.SetStudentId("A1");
	student1.SetFirstName("John");
	student1.SetLastName("Smith");
	student1.SetEmail("John1989@gm ail.com");
	student1.SetAge(20);
	student1.SetNumberOfDays(30, 35, 40);
	student1.SetDegreeProgram(SECURITY);
	student1.Print();
	*/

	/*
	//Test for roster.h and roster.cpp to ensure it works
	Roster roster1;
	roster1.ParseData(studentData);
	//roster1.remove("A3");
	//roster1.printAll();
	//roster1.remove("A3");
	//roster1.printAverageDaysInCourse("A3");
	//roster1.printInvalidEmails();
	//roster1.printByDegreeProgram(SOFTWARE);
	roster1.printAll();
	*/
	
	
	Roster classRoster;
	classRoster.ParseData(studentData); //this adds the studentData into the classRosterArray within the Roster class

	classRoster.printAll();
	classRoster.printInvalidEmails();

	//create for loop to loop through each student id
	cout << "Average Day In Course: " << endl;
	for (int i = 1; i < 6; i++)
	{
		classRoster.printAverageDaysInCourse("A" + to_string(i));
	} 
	cout << endl;


	classRoster.printByDegreeProgram(SOFTWARE);
	
	classRoster.remove("A3");
	classRoster.printAll();
	classRoster.remove("A3");


	return 0;
}
