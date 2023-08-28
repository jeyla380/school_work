import java.util.Scanner; 

public class LabProgram {
   public static void main(String[] args) {
      
      Scanner scnr = new Scanner(System.in);
      
      String name = scnr.nextLine();
      String[] nameSplit = name.split(" ", 3);
      
      //for (String x : nameSplit)
         //System.out.println(x);
      
      if (nameSplit.length == 2)
      {
         String firstName = nameSplit[0];
         String lastName = nameSplit[1];
         
         //System.out.printf("%s, %s", lastName, firstName);
         char[] firstNameList = firstName.toCharArray();
         char firstNameLetter = firstNameList[0];
         
         System.out.printf("%s, %c.%n", lastName, firstNameLetter);
      }
      else
      {
         String firstName = nameSplit[0];
         String middleName = nameSplit[1];  
         String lastName = nameSplit[2];
         
         //System.out.printf("%s, %s %s", lastName, firstName, middleName);
         char[] firstNameList = firstName.toCharArray();
         char[] middleNameList = middleName.toCharArray();
         
         char firstNameLetter = firstNameList[0];
         char middleNameLetter = middleNameList[0];
         
         System.out.printf("%s, %c.%c.%n", lastName, firstNameLetter, middleNameLetter);
      }
   }
}
