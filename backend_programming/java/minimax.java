package MinMax;

import java.util.Scanner;

public class minimax {


    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);


        System.out.println("Choose the first integer: ");
        int number1 = input.nextInt();

        System.out.println("Choose the second integer: ");
        int number2 = input.nextInt();


        if (number1 == number2)
            System.out.printf("%d is equal to %d\n", number1, number2);

        if (number1 > number2)
            System.out.printf("%d is greater than %d\n", number1, number2);

        if (number1 >= number2)
            System.out.printf("%d is greater than or equal to %d\n", number1, number2);

        if (number1 < number2)
            System.out.printf("%d is less than %d\n", number1, number2);

        if (number1 <= number2)
            System.out.printf("%d is less than or equal to %d\n", number1, number2);

        if (number1 != number2)
            System.out.printf("%d does not equal %d", number1, number2);

    }

}
