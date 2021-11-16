package Midterm2;

import java.util.Random;

public class RandomNumbers {

    public static void main(String[] args){

        Random rand = new Random();
        int number;


        for (int i = 1; i <= 49; i++){

            number = (rand.nextInt(66)+ 10) * 10;
            System.out.printf("%-5d ", number);

            if(0 == i % 7){
                System.out.println();
            }
        }
        System.out.println();

    }
}
