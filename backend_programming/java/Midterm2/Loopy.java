/*
Jessemy Lake
CSIS 1400
 */

package Midterm2;

public class Loopy {

    public static void main(String[] args){

        /*
        n1(0)  n2(*)  n3(%) i
        9       1       0   0     0 0 0 0 0 0 0 0 0 *
        7       1       2   1     0 0 0 0 0 0 0 * % %
        5       1       4   2     0 0 0 0 0 * % % % %
        3       1       6   3     0 0 0 * % % % % % %
        1       1       8   4     0 * % % % % % % % %

        n1 = 9 - 2i
        n2 = 1
        n3 = 2i
         */

        for(int i = 0; i < 5; i++){

            for(int j = 9 - (2 * i); j > 0; j--){

                System.out.print("0 ");
            }

            for(int k = 1; k == 1; k++){

                System.out.print("* ");
            }

            for(int m = 0; m < (2 * i); m++){

                System.out.print("% ");
            }

            System.out.println();

        }
    }
}
