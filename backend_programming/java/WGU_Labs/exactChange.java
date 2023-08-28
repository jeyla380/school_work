import java.util.Scanner; 

public class LabProgram {
   public static void main(String[] args) {
      /* Type your code here. */
      
      Scanner scnr = new Scanner(System.in);
      int change = scnr.nextInt();
      
      if (change == 0)
      {
         System.out.println("No change");   
      }
      else
      {
         int dollars;
         int quarters;
         int dimes;
         int nickels;
         int pennies;
         
         dollars = change / 100;
         change = change - (dollars * 100);
         if (dollars > 1)
         {
            System.out.printf("%d Dollars%n", dollars);   
         }
         else if (dollars == 1)
         {
            System.out.printf("%d Dollar%n", dollars);   
         }
         
         quarters = change / 25;
         change = change - (quarters * 25);
         if (quarters > 1)
         {
            System.out.printf("%d Quarters%n", quarters);   
         }
         else if (quarters == 1)
         {
            System.out.printf("%d Quarter%n", quarters);   
         }
         
         dimes = change / 10;
         change = change - (dimes * 10);
         if (dimes > 1)
         {
            System.out.printf("%d Dimes%n", dimes);   
         }
         else if (dimes == 1)
         {
            System.out.printf("%d Dime%n", dimes);   
         }
         
         nickels = change / 5;
         change = change - (nickels * 5);
         if (nickels > 1)
         {
            System.out.printf("%d Nickels%n", nickels);   
         }
         else if (nickels == 1)
         {
            System.out.printf("%d Nickel%n", nickels);   
         }
         
         pennies = change / 1;
         change = change - (pennies * 1);
         if (pennies > 1)
         {
            System.out.printf("%d Pennies%n", pennies);   
         }
         else if (pennies == 1)
         {
            System.out.printf("%d Penny%n", pennies);   
         }
      }
   }
}
