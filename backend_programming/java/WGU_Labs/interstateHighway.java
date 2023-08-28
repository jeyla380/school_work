import java.util.Scanner; 

public class LabProgram {
   public static void main(String[] args) {
      Scanner scnr = new Scanner(System.in); 
      int highwayNumber;
      int primaryNumber;

      highwayNumber = scnr.nextInt();
      
      //Notes 0 and 100, 200
      if (highwayNumber == 0 || highwayNumber % 100 == 0)
      {
         System.out.printf("%d is not a valid interstate highway number.%n", highwayNumber);   
      }
      
      //primary highways: 1-99 (north/south for evens, east/west for odds)
      else if (highwayNumber >= 1 && highwayNumber <= 99)
      {
         if (highwayNumber % 2 == 0)
         {
            System.out.printf("I-%d is primary, going east/west.%n", highwayNumber);
         }
         else
         {
            System.out.printf("I-%d is primary, going north/south.%n", highwayNumber);
         }
      }
      //auxiliary highways: 100-999 (east/west) serving the last digit (or last two digits) which are the primary highways
      else if (highwayNumber >= 100 && highwayNumber <= 999)
      {
         if (highwayNumber % 2 == 0)
         {
            primaryNumber = (Math.abs(highwayNumber) % 100);
            System.out.printf("I-%d is auxiliary, serving I-%d, going east/west.%n", highwayNumber, primaryNumber);   
         }
         else
         {
            primaryNumber = (Math.abs(highwayNumber) % 10);
            System.out.printf("I-%d is auxiliary, serving I-%d, going north/south.%n", highwayNumber, primaryNumber);
         }
      }
   }
}
