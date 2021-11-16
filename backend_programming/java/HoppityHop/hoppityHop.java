package HoppityHop;

import java.util.Scanner;

public class hoppityHop {

    public static void main(String[] args){

        /*
        1. Use the loop statements: for, while, or do/while
        2. Start with n = 1
        3. Use n+1, up to 25 (n<26 or n<=25)
        4. For every multiple of 3, use n%3=0
        5. For every multiple of 5, use n%5=0
            With every multiple of 3, "hoppity" is said
            With every multiple of 5, "hop" is said
         */


        for(int n = 1; n <= 25; n++) {

            if (n % 3 == 0 && n % 5 == 0) {
                System.out.println("Hoppity Hop");
            }
            else if (0 == n % 3) {
                System.out.println("Hoppity");
            }
            else if(0 == n % 5){
                System.out.println("Hop");
            }
            else{
                System.out.println(n);
            }
        }




    }
}
