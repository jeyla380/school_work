package Marbles;

import java.util.Scanner;

public class marble {

    public static void main(String[] args){

        Scanner input = new Scanner(System.in);
        Scanner number = new Scanner(System.in);


        System.out.println("Choose the first color:");
        String color1 = input.nextLine();

        System.out.println("Choose the next color:");
        String color2 = input.nextLine();

        System.out.println("Choose the last color:");
        String color3 = input.nextLine();


        System.out.printf("How many %s marbles are there? %n", color1);
        int num1 = number.nextInt();

        System.out.printf("How many %s marbles are there? %n", color2);
        int num2 = number.nextInt();

        System.out.printf("How many %s marbles are there? %n", color3);
        int num3 = number.nextInt();


        System.out.println();
        System.out.println();


        String heading1 = "Color";
        String heading2 = "Number of Marbles";
        System.out.printf("%-12s %-10s %n", heading1, heading2);


        System.out.println("- - - - - - - - - - - - - - - -");


        System.out.printf("%-12s %-10s %n", color1, num1);
        System.out.printf("%-12s %-10s %n", color2, num2);
        System.out.printf("%-12s %-10s %n", color3, num3);
    }
}
