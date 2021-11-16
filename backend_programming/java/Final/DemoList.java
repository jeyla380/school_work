/*
Jessemy Lake
CSIS 1400
 */

package Final1400;

import java.util.ArrayList;

public class DemoList {

    public static void main(String[] args){

        ArrayList<Integer> numbers = new ArrayList<>();

        numbers.add(5);
        numbers.add(7);
        numbers.add(2);
        numbers.add(8);
        numbers.add(10);
        numbers.add(45);

        System.out.println("List: " + numbers);

        numbers.remove(5);
        int sum = 0;
        for(int i : numbers){
            sum += i;
        }
        System.out.println("Sum of the elements in the list: " + sum);

        numbers.set(4, 18);
        numbers.remove(3);
        System.out.println("List: " + numbers);
    }
}
