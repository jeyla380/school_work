import java.util.Scanner;

public class LabProgram {
   
   public static void swapValues(int[] values)
   {
      int tempOne = 0;
      int tempTwo = 0;
      
      tempOne = values[1];
      values[1] = values[0];
      values[0] = tempOne;
      
      tempTwo = values[3];
      values[3] = values[2];
      values[2] = tempTwo;
      
      for (int i = 0; i < values.length; i++)
      {
         if (values[i] == values[values.length-1])
         {
            System.out.printf("%d", values[i]);   
         }
         else
         {
            System.out.printf("%d ", values[i]);   
         }
      }
   }
   
   public static void main(String[] args) {
      
      Scanner scnr = new Scanner(System.in);
      int[] userValues = new int[4];
      
      int tempOne = 0;
      int tempTwo = 0;
      
      for (int i = 0; i < userValues.length; i++)
      {
         userValues[i] = scnr.nextInt(); 
      }
      
      swapValues(userValues);
      System.out.println();

   }
}
