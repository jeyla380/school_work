package Employee;

public class Employee
{

    private String firstName;
    private String lastName;
    private double salary;
   // fields


    public Employee(String lName, String fName, double s){

        lastName = lName;
        firstName = fName;
        setSalary(s);
            //will drop down to setSalary and complete the lines there & then continue up to the top
    }
	// constructors


    public String getFirstName(){

        return firstName;
    }

    public String getLastName(){

        return lastName;
    }

    public double getSalary(){

        return salary;
    }

    public void setSalary(double s){

        if (s>=0)
            salary = s;
    }
   // methods	

}