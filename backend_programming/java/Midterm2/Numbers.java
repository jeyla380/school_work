/*
Jessemy Lake
CSIS 1400
 */

package Midterm2;

import java.util.Random;

public class Numbers {

    public static void main(String[] args){

        Random rand = new Random();

        int number;


        for(int i = 1; i <= 25; i++){


            number = (rand.nextInt(13)*3) + 6;

            switch(number){
                case 18:
                    System.out.printf("%-5s", "__ ");
                    break;
                case 33:
                    System.out.printf("%-5s", "all your base ");
                    break;
                default:
                    System.out.printf("%-5d", number);
                    break;
            }

            if(number == 33){
                break;
            }

            if(0 == i % 5){
                System.out.println();
            }

        }
        System.out.println();



    }
}
