import java.util.Scanner; 

public class LabProgram {
   public static void main(String[] args) {
      
      Scanner scnr = new Scanner(System.in);
      
      int maxNum = 0;
      double averageNum = 0;
      
      int i = 1;
      int count = 0;
      double temp = 0;
      
      while (i > 0)
      {
         int inputNum = scnr.nextInt();
         if (inputNum < 0)
         {
            i = 0; //or 'break;' works
         }
         else
         {
            //finding average
            temp = temp + inputNum;
            count++;
            
            //finding max
            if (inputNum > maxNum)
            {
               maxNum = inputNum;   
            }
         }
      }
      averageNum = temp / count;
      //System.out.println(averageNum);
      //System.out.println(maxNum);
      System.out.printf("%d %.2f%n", maxNum, averageNum);
   }
}
