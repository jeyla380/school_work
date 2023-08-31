import java.util.Scanner;

public class LabProgram {
   public static void main(String[] args) {
      
      Scanner scnr = new Scanner(System.in);
      
      int i = 1;
      while (i > 0)
      {
         String inputString = scnr.nextLine();
         
         if (inputString.equals("Done") || inputString.equals("done") || inputString.equals("d"))
         {
            i = 0;
         }
         else
         {
            char[] stringList = inputString.toCharArray();
            //for (char j : stringList)
               //System.out.printf("%c", j); 
               
            for (int j = stringList.length - 1; j >= 0; j--)
            {
               System.out.printf("%c", stringList[j]);   
            }
            
            System.out.println();   
         }
      }


   }
}
