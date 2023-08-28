import java.util.Scanner;

public class LabProgram {
   public static void main(String[] args) {
      Scanner scnr = new Scanner(System.in);
      int inputYear;
      boolean isLeapYear;
      
      isLeapYear = false;
      inputYear = scnr.nextInt();
      
      //1) year must be divisible by 4 (if not century year)
      if (inputYear % 100 != 0)
      {
         if (inputYear % 4 == 0)
         {
            isLeapYear = true;
            System.out.printf("%d - leap year%n", inputYear);
         }
         else
         {
            System.out.printf("%d - not a leap year%n", inputYear); 
         }
      }
      //2) if century year (1600, 1700, 1800, etc.), must be divisible by 400
      else if (inputYear % 100 == 0)
      {
         if (inputYear % 400 == 0)
         {
            isLeapYear = true;
            System.out.printf("%d - leap year%n", inputYear);
         }
         else
         {
            System.out.printf("%d - not a leap year%n", inputYear);   
         }
      }
      else
      {
         System.out.printf("%d - not a leap year%n", inputYear); 
      }
   }
}
