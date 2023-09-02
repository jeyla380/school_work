import java.util.Scanner;
import java.util.Random;

public class LabProgram {
   
   public static String coinFlip(Random rand)
   {
      int randNum = rand.nextInt(2);
      if (randNum == 1) //heads
      {
         return "Heads";
      }
      else //tails
      {
         return "Tails";   
      }
   }
   
   public static void main(String[] args) {
      Scanner scnr = new Scanner(System.in);
      Random rand = new Random(2); // Unique seed
      
      int inputNum = scnr.nextInt();
      
      
      
      for (int i = 0; i < inputNum; i++)
      {
         System.out.println(coinFlip(rand)); 
      }
   }
}
