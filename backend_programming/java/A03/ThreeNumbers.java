package A03;

import java.util.Scanner;

public class ThreeNumbers {

    public static void main(String[] args){

        Scanner input = new Scanner(System.in);

        System.out.print("Enter the 1st number: ");
        int n1 = input.nextInt();
        System.out.print("Enter the 2nd number: ");
        int n2 = input.nextInt();
        System.out.print("Enter the 3rd number: ");
        int n3 = input.nextInt();

        System.out.println();


        System.out.printf("All 3 numbers: %d %d %d\n", n1, n2, n3);


        if (n1 < n2 && n2 < n3) {
            System.out.printf("Sorted numbers: %d %d %d", n1, n2, n3);
        }

        if (n1 > n2 && n1 < n3) {
            System.out.printf("Sorted numbers: %d %d %d", n2, n1, n3);
        }

        if (n1 < n2 && n2 > n3) {
            System.out.printf("Sorted numbers: %d %d %d", n1, n3, n2);
        }

        if (n1 > n2 && n1 > n3) {
            System.out.printf("Sorted numbers: %d %d %d", n2, n3, n1);
        }

        if (n3 < n2 && n2 < n1) {
            System.out.printf("Sorted numbers: %d %d %d", n3, n2, n1);
        }

        if (n3 < n1 && n1 < n2) {
            System.out.printf("Sorted numbers: %d %d %d", n3, n1, n2);
        }


    }
}
