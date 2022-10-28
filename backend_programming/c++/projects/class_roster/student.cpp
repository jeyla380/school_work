#include <iostream>
#include <string>
using namespace std;

#include "student.h"
#include "degree.h"
#include "roster.h"

Student::Student(string sId, string fName, string lName, string emailAdd, int ageNum, int courseDay1, int courseDay2, int courseDay3, DegreeProgram degreeType) //constructor
{
	studentId = sId;
	firstName = fName;
	lastName = lName;
	email = emailAdd;
	age = ageNum;
	day1 = courseDay1;
	day2 = courseDay2;
	day3 = courseDay3;
	degreeProgram = degreeType;
}

Student::Student() //default constructor
{
	studentId = "N/A";
	firstName = "N/A";
	lastName = "N/A";
	email = "N/A";
	age = 0;
	day1 = 0;
	day2 = 0;
	day3 = 0;
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
void Student::SetCourseDays1(int day1)
{
	this->day1 = day1;
}
int Student::getCourseDays1() const
{
	return day1;
}

void Student::SetCourseDays2(int day2)
{
	this->day2 = day2;
}
int Student::getCourseDays2() const
{
	return day2;
}

void Student::SetCourseDays3(int day3)
{
	this->day3 = day3;
}
int Student::getCourseDays3() const
{
	return day3;
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
