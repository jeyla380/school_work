package Random;

import java.util.Random;

public class LabRandom {

    public static void main(String[] args){

        Random rand = new Random();

        int number;

        for(int i = 1; i <= 100; i++){

            number = rand.nextInt(4)+4;
            System.out.printf("%-5d", number);

            if(i % 10 == 0){
                System.out.println();
            }
        }
        System.out.println();

        for(int i = 1; i <= 100; i++){

            number = rand.nextInt(9)*10 + 10;
            System.out.printf("%-5d", number);

            if(i % 10 == 0){
                System.out.println();
            }
        }
        System.out.println();

        for(int i = 1; i <= 100; i++){

            number = rand.nextInt(99)+901;
            System.out.printf("%-5d", number);

            if(i % 10 == 0){
                System.out.println();
            }
        }
    }
}
