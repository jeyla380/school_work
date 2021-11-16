package A02;

import java.util.Scanner;

public class SkiTickets {

    public static void main(String[] args){

        Scanner input = new Scanner(System.in);

        int adultTickets = 93;
        int youthTickets = 47;

        System.out.print("Enter amount of adult tickets: ");
        int adult = input.nextInt();
        System.out.print("Enter amount of youth tickets: ");
        int youth = input.nextInt();
        System.out.print("Enter name: ");
        String name = input.next();

        System.out.println();

        System.out.printf("Number of adult tickets: %d\n", adult);
        System.out.printf("Number of youth tickets: %d\n", youth);
        System.out.printf("Name: %s", name);

        System.out.println();
        System.out.println();

        int totalAdultTickets = (adult * adultTickets);
        int totalYouthTickets = (youth * youthTickets);
        int totalTickets = (totalAdultTickets + totalYouthTickets);

        System.out.printf("Invoice for %s: %n", name);
        System.out.println();
        System.out.printf("Adult: %d . . . $%d\n", adult, totalAdultTickets);
        System.out.printf("Youth: %d . . . $%d\n", youth, totalYouthTickets);
        System.out.print("- - - - - - - - - - -\n");
        System.out.printf("                $%s\n",totalTickets);
        System.out.print("               = = = = ");
    }
}
