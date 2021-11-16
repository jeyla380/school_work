package Midterm1;

import java.util.Scanner;

public class VariableandScanner {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.print("Please input a city name, the population, and the area.\n");

        String city = input.nextLine();
        int population = input.nextInt();
        int area = input.nextInt();

        System.out.printf("City: %s\n", city);
        System.out.printf("Population: %d\n", population);
        System.out.printf("Area: %d\n", area);
        System.out.println();

        int squaremile = population / area;

        System.out.printf("The city is %s\n", city);
        System.out.printf("There are %d people per square mile", squaremile);

    }
}
