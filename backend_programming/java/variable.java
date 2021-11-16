package Variables;

import java.util.Scanner;

public class variable {

    public static void main(String[] args){

        Scanner myDestination = new Scanner(System.in);


        String destination = myDestination.nextLine();

        System.out.printf("Favorite Destination: %s", destination);

        System.out.println();
        System.out.printf("Welcome to %s", destination);

        System.out.println();
        System.out.println();


        int Kingspeak = 4124;
        int Timponogos = 3581;

        System.out.println();
        System.out.println();


        System.out.printf("Elevation of Kings Peak: %d", Kingspeak);
        System.out.println();
        System.out.printf("Elevation of Timponogos: %d", Timponogos);

    }
}
