import java.util.Scanner;

public class LabProgram {
   public static void main(String[] args) {

   int letterCount = 0;
   
   Scanner scnr = new Scanner(System.in);
   String inputString = scnr.nextLine();
   String[] stringList = inputString.split(" ", 2);
   
   char letter = stringList[0].charAt(0);
   String sentence = stringList[1];
   
   char[] sentenceLetters = sentence.toCharArray();
   for (char i : sentenceLetters)
      if (letter == i)
      {
         letterCount++;   
      }
   
   if (letterCount == 1)
   {
      System.out.printf("%d %c%n", letterCount, letter);
   }
   else
   {
      System.out.printf("%d %c's%n", letterCount, letter);
   }
   
   }
}
