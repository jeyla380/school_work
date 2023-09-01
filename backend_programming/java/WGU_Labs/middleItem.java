import java.util.Scanner; 

public class LabProgram {
   public static void main(String[] args) {
      Scanner scnr = new Scanner(System.in);
      int[] userValues = new int[9];  // Set of data specified by the user      
      int[] intValues;
      
      int midInt = 0;
      int i = 0;
      
      while (i < userValues.length)
      {
         int inputNum = scnr.nextInt();
         if (inputNum < 0)
         {
            i = userValues.length;
         }
         else
         {
            //System.out.println(inputNum);  
            userValues[i] = inputNum;

         }
         i++;
      }
      
      int count = 0;
      for (int k = 0; k < userValues.length; k++)
      {
         if (userValues[k] != 0)
         {
            count++;
            //System.out.println(userValues[k]);   
         }
      }
      midInt = userValues[count / 2];
      System.out.printf("Middle item: %d%n", midInt);
      
   }
}
