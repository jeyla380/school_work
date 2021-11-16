package Midterm1.KangarooPackage;

public class KangarooApp {

    public static void main(String[] args){

        Kangaroo myKangaroo = new Kangaroo();

        myKangaroo.setWeight(60);
        int kweight = myKangaroo.getWeight();
        System.out.println("MyKangaroo weighs " + kweight + "kg.");

        myKangaroo.jump();

        kweight = kweight + 15;
        System.out.println("MyKangaroo now weighs " + kweight + "kg.");


    }
}
