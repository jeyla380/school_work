import java.util.Scanner;

public class LabProgram {
   public static void main(String[] args) {
      Scanner scnr = new Scanner(System.in);
      VendingMachine vendmach = new VendingMachine();
      
      vendmach.purchase(scnr.nextInt());
      vendmach.restock(scnr.nextInt());
      vendmach.report();
   }
}
