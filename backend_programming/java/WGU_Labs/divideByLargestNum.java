import java.util.Scanner; 

public class LabProgram {
   public static void main(String[] args) {
      
      double[] userValues = new double[20];
      Scanner scnr = new Scanner(System.in);
      
      int firstNum = scnr.nextInt();
      double largestValue = 0;
      
      for (int i = 0; i < firstNum; i++)
      {
         userValues[i] = scnr.nextDouble();
         if (userValues[i] > largestValue)
         {
            largestValue = userValues[i];   
         }
      }
      //System.out.println(largestValue);
      
      for (int j = 0; j < firstNum; j++)
      {
         userValues[j] = userValues[j] / largestValue;
         System.out.printf("%.2f ", userValues[j]);
      }
      System.out.println();
   }
}
