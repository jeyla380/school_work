package LabPattern3;

public class Pattern3 {

    /*
    n1 ("o")    n2 (".")    i        column #
    5           0           0 (1)      5                   OOOOO
    4           1           1 (2)      5                   OOOO.
    3           2           2 (3)      5                   OOO..
    2           3           3 (4)      5                   OO...
    1           4           4 (5)      5                   O....

    i--         i++
    n2 = i
    n1 = j = 5 - i
    n2 = k = 5 + i
     */

    public static void main(String[] args){

        for(int i = 0; i < 5; i++){

            for(int j = 5 - i; j > 0; j--){

                System.out.print("o ");
            }

            for(int k = 0; k < i; k++) {

                System.out.print(". ");
            }

            System.out.println();
        }

    }

}
