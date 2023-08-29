import java.util.Scanner; 

public class LabProgram {
   public static void main(String[] args) {
      
      Scanner scnr = new Scanner(System.in);
      int inputNum = scnr.nextInt();
      String reverseBinaryNum = "";
      
      while (inputNum > 0)
      {
         reverseBinaryNum = reverseBinaryNum + Integer.toString(inputNum % 2);
         inputNum = inputNum / 2;  
      }
      System.out.println(reverseBinaryNum);
   }
}
