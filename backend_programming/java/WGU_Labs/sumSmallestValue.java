import java.util.Scanner; 

public class LabProgram {
   public static void main(String[] args) {
      Scanner scnr = new Scanner(System.in);     
      int inputNum;
      int smallestNum = Integer.MAX_VALUE;
      int sum = 0;
      
      int i = 1;
      while (i > 0)
      {
         inputNum = scnr.nextInt();  
         if (inputNum < 0)
         {
            i = 0;   
         }
         else
         {
            //find sum
            sum = sum + inputNum;
            
            //find smallest num
            if (inputNum < smallestNum)
            {
               smallestNum = inputNum;   
            }
            else
            {
               continue;   
            }
         }
      }
      
      System.out.printf("Smallest: %d%n", smallestNum);
      System.out.printf("Sum: %d%n", sum);
      
   }
}
