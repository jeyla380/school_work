package Final1400;

import java.util.Arrays;

public class DemoArray {

    enum Fruit{
        BANANA,
        PEACH,
        PLUM,
        APPLE,
        ORANGE,
        GRAPEFRUIT;
    }

    public static void main(String[] args){

        Fruit[] fruitie = new Fruit[7];
        fruitie[0] = Fruit.BANANA;
        fruitie[1] = Fruit.GRAPEFRUIT;
        fruitie[2] = Fruit.APPLE;
        fruitie[3] = Fruit.PLUM;
        fruitie[4] = Fruit.PEACH;
        fruitie[5] = Fruit.ORANGE;
        fruitie[6] = Fruit.PLUM;

        System.out.println("Fruits: " + Arrays.toString(fruitie));
        System.out.println("First Fruit: " + Fruit.BANANA);
        System.out.println("Last Fruit: " + Fruit.PLUM);

        fruitie[1] = Fruit.BANANA;
        System.out.println("Updated Fruits: " + Arrays.toString(fruitie));
        System.out.println("Size: " + fruitie.length);

    }
}
