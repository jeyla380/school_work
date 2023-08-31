import java.util.Scanner;

public class LabProgram {
   public static void main(String[] args) {
      
      Scanner scnr = new Scanner(System.in);
      String inputString = scnr.nextLine();
      char[] stringChars = inputString.toCharArray();
      
      for (char i : stringChars)
         if (Character.isAlphabetic(i))
         {
            System.out.printf("%c", i);   
         }
      System.out.println();
   }
}
