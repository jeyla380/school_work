#include <iostream>
#include <string>
#include <tuple>
using namespace std;

#include "student.h"
#include "degree.h"
#include "roster.h"

Student::Student(string sId, string fName, string lName, string emailAdd, int ageNum, int *courseDays, DegreeProgram degreeType) //constructor
{
	studentId = sId;
	firstName = fName;
	lastName = lName;
	email = emailAdd;
	age = ageNum;
	//day1 = courseDay1;
	//day2 = courseDay2;
	//day3 = courseDay3;
	for (int i = 0; i < 3; i++)
	{
		days[i] = courseDays[i]; //this copies the courseDays[i] data over to the days[i], this will cause issues with element 1 and 2 (not 0) if there is no for loop
	}
	degreeProgram = degreeType;
}

Student::Student() //default constructor
{
	studentId = "N/A";
	firstName = "N/A";
	lastName = "N/A";
	email = "N/A";
	age = 0;
	for (int i = 0; i < 3; i++) //each day will equal 0
	{
		days[i] = 0;
	}
	degreeProgram = SECURITY;
}

void Student::SetStudentId(std::string studentId)
{
	this->studentId = studentId; //this->studentId = private data member studentId in student.h
}
string Student::getStudentId() const
{
	return studentId;
}

void Student::SetFirstName(std::string firstName)
{
	this->firstName = firstName; //this->firstName = private data member firstName in student.h
}
string Student::getFirstName() const
{
	return firstName; //returns private data member firstName
}

void Student::SetLastName(std::string lastName)
{
	this->lastName = lastName; //this->lastName = private data member lastName in student.h
}
string Student::getLastName() const
{
	return lastName;
}

void Student::SetEmail(std::string email)
{
	this->email = email;
}
string Student::getEmail() const
{
	return email;
}

void Student::SetAge(int age)
{
	this->age = age;
}
int Student::getAge() const
{
	return age;
}

//number of days spent in first course
void Student::SetCourseDays(int days[3])
{
	for (int i = 0; i < 3; i++)
	{
		this->days[i] = days[i];
	}
}
int Student::getCourseDays1() const
{
	return days[0];
}
int Student::getCourseDays2() const
{
	return days[1];
}
int Student::getCourseDays3() const
{
	return days[2];
}

//type of CS program
void Student::SetDegreeProgram(DegreeProgram degreeProgram)
{
	this->degreeProgram = degreeProgram;
}
DegreeProgram Student::getDegreeProgram() const
{
	return degreeProgram;
}

void Student::Print()
{
	
	cout << getStudentId() << '\t';
	cout << "First Name: " << getFirstName() << '\t';
	cout << "Last Name: " << getLastName() << '\t';
	cout << "Age: " << getAge() << '\t';
	cout << "daysInCourse: {" << getCourseDays1() << ", " << getCourseDays2() << ", " << getCourseDays3() << "}";


	//this turns the values of the enum and turns them into strings
	const char* type[] = { "Security", "Network", "Software" };
	string degreeType;
	if (getDegreeProgram() == 0)
	{
		degreeType = type[SECURITY];
	}
	else if (getDegreeProgram() == 1)
	{
		degreeType = type[NETWORK];
	}
	else
	{
		degreeType = type[SOFTWARE];
	}
	cout << " Degree Program: " << degreeType << endl;
}
