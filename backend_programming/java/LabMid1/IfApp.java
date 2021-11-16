package Midterm1;

import java.util.Scanner;

public class IfApp {

    public static void main(String[] args){

        Scanner input = new Scanner(System.in);

        System.out.print("Enter the first number, n1: ");
        int n1 = input.nextInt();
        System.out.print("Enter the second number, n2: ");
        int n2 = input.nextInt();

        System.out.println();

        if(n1 != n2){
            System.out.printf("n1: %d, n2: %d\n", n1, n2);
        }

        if(n2 == 2*n1){
            System.out.printf("%d is twice as big as %d\n", n2, n1);
        }

        if(n1 == 2*n2){
            System.out.printf("%d is twice as big as %d\n", n1, n2);
        }


    }
}
