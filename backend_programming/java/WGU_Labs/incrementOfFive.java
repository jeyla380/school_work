import java.util.Scanner;

public class LabProgram {
   public static void main(String[] args) {
      
      Scanner scnr = new Scanner(System.in);
      String inputInts = scnr.nextLine();
      String[] splitInput = inputInts.split(" ", 2);
      
      int firstNum = Integer.parseInt(splitInput[0]);
      int secondNum = Integer.parseInt(splitInput[1]);
      int incrementFive = 0;
      
      if (secondNum < firstNum)
      {
         System.out.println("Second integer can't be less than the first.");   
      }
      else
      {
         int i = 1;
         incrementFive = firstNum;
         
         while (i > 0)
         {
            if (firstNum % 5 == 0 && secondNum % 5 == 0)
            {
               if (incrementFive == secondNum)
               {
                  System.out.printf("%d %n", incrementFive);
                  i = 0;   
               }
               else
               {
                  System.out.printf("%d ", incrementFive);
                  incrementFive = incrementFive + 5;
               }
            }
            else
            {
               if (incrementFive > firstNum && incrementFive < secondNum)
               {
                  System.out.printf("%d %n", incrementFive); 
                  i = 0;
               }
               else if (firstNum == secondNum)
               {
                  System.out.printf("%d %n", incrementFive); 
                  i = 0;
               }
               else
               {
                  System.out.printf("%d ", incrementFive);
                  incrementFive = incrementFive + 5;  
               }
            }
         }
   
   
      }
   }
}
