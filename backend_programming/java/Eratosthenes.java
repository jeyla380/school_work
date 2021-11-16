package LabEratosthenes;

import java.util.Arrays;

public class Eratosthenes {

    public static void main(String[] args) {

        //create a for loop to step through all 120 slots in marked
        //say every number is prime & check off the list
        boolean marked[] = new boolean[120];
        marked[0] = false;
        for(int i = 1; i < 120; i++){

            // check if marked[i] is true
            marked[i] = true;
        }

        //check every number >= 2 & <= 120 if prime
        for(int i = 2; i <= 120; i++){

            //i is prime if it hasn't been marked; (need to subject 1 from the index)
            //if below is true, then we have a prime number
            if(marked[i - 1]){

                System.out.println(i);

                // for loop to create multiplication table 2x2, 2x3, 2x4.. until 2*X > 120
                //mark multiples of i
                //below is more efficient than 2 * i
                for(int j = i * i; j <= 120; j += i){

                    // mark the multiples of i. marked[i*j]
                    marked[j - 1] = false;
                }
            }

        }
        System.out.println();



    }

}
