import java.util.Scanner;

public class LabProgram {
   public static void main(String[] args) {
      /* Type your code here. */
      Scanner scnr = new Scanner(System.in);
      
      int numOne = scnr.nextInt();
      int numTwo = scnr.nextInt();
      int numThree = scnr.nextInt();
      
      if (numOne <= numTwo && numOne <= numThree)
      {
         System.out.println(numOne);
      }
      else if (numTwo <= numThree && numTwo <= numOne)
      {
         System.out.println(numTwo);
      }
      else if (numThree <= numOne && numThree <= numTwo)
      {
         System.out.println(numThree);
      }
   }
}

