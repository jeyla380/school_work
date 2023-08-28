import java.util.Scanner;

public class LabProgram {

	public static void main(String[] args) {

		Scanner scnr = new Scanner(System.in);
      String information = scnr.nextLine();
      //System.out.println(information);
      
      String[] listOfInfo = information.split(" ", 3);
      //for (String x : listOfInfo)
         //System.out.println(x);
         
      String firstName = listOfInfo[0];
      String lastName = listOfInfo[1];
      int fourDigits = Integer.valueOf(listOfInfo[2]);
      //System.out.println(fourDigits);
      
      char[] firstNameList = firstName.toCharArray();
      String firstNameUser = "";
      if (firstNameList.length > 6)
      {
         for (int i = 0; i < 6; i++)
         {
            firstNameUser = firstNameUser + firstNameList[i];   
         }
      }
      else if (firstNameList.length <= 6)
      {
         for (char i : firstNameList)
            firstNameUser = firstNameUser + i;  
      }
      //System.out.println(firstNameUser);
      
      char[] lastNameList = lastName.toCharArray();
      char lastNameLetter = lastNameList[0];
      
      int lastDigit = fourDigits % 10;
      //System.out.println(lastDigit);
      
      System.out.printf("Your login name: %s%c_%d%n", firstNameUser, lastNameLetter, lastDigit);
	}
}
