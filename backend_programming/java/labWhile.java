package LabWhile;

import java.util.Scanner;

public class labWhile {

    public static void main(String[] args){

        multiplyNumbers();
    }

    public static void multiplyNumbers(){
        Scanner input = new Scanner(System.in);

        int product = 1;
        System.out.println("Enter a number. Press 0 to quit.");
        int number = input.nextInt();


        while(number != 0){

            product = number * product;
            System.out.println("Enter a number. Press 0 to quit.");
            number = input.nextInt();

            //if(number == 0){
            //  break;

        }
        System.out.print(product);

    }
}
