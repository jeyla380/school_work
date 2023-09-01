import java.util.Scanner; 

public class LabProgram {
   public static void main(String[] args) {
      Scanner scnr = new Scanner(System.in);
      int[] userValues = new int[20];   // List of integers from input

      int firstNum = scnr.nextInt();
      
      for (int i = 0; i < firstNum; i++)
      {
         userValues[i] = scnr.nextInt(); 
         //System.out.println(userValues[i]);
      }
      
      int lastNum = scnr.nextInt();
      //System.out.println(lastNum);
      
      for (int i = 0; i < firstNum; i++)
      {
         if (userValues[i] <= lastNum)
         {
            System.out.printf("%d,", userValues[i]);   
         }
      }
      System.out.println();
   }
}
