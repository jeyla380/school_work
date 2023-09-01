import java.util.Scanner;

public class LabProgram {
   public static void main(String[] args) {
      
      Scanner scnr = new Scanner(System.in);
      int inputNum = scnr.nextInt();
      
      String inputString = scnr.nextLine();
      inputString = inputString.trim();
      String[] words = inputString.split(" ", inputNum + 1);
      
      char letter = words[words.length - 1].charAt(0);
      //System.out.println(letter);
      
      for (int i = 0; i < words.length; i++)
      {
         if (words[i] != words[words.length - 1])
         {
            //System.out.println(words[i]);
            if (words[i].indexOf(letter) != -1)
            {
               System.out.printf("%s,", words[i]);   
            }
         }
      }
      System.out.println();
   }
}
