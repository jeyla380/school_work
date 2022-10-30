#include <iostream>
#include <string>
#include "degree.h"

#ifndef STUDENTH
#define STUDENTH

class Student
{
public:
	Student(std::string studentId, std::string firstName, std::string lastName, std::string email, int age, int days[3], DegreeProgram degreeProgram); //constructor
	Student(); //default constructor

	void SetStudentId(std::string studentId);
	std::string getStudentId() const;

	void SetFirstName(std::string firstName);
	std::string getFirstName() const;

	void SetLastName(std::string lastName);
	std::string getLastName() const;

	void SetEmail(std::string email);
	std::string getEmail() const;

	void SetAge(int age);
	int getAge() const;

	void SetCourseDays(int days[3]);
	int getCourseDays1() const;
	int getCourseDays2() const;
	int getCourseDays3() const;

	void SetDegreeProgram(DegreeProgram degreeProgram);
	DegreeProgram getDegreeProgram() const;

	void Print();

private:
	std::string studentId;
	std::string firstName;
	std::string lastName;
	std::string email;
	int age;
	int days[3];
	//int day1;
	//int day2;
	//int day3;
	DegreeProgram degreeProgram;
};

#endif
