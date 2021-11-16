package Parrot;

import java.util.Scanner;

public class parrotTest {

    public static void main(String[] args){

        Scanner input = new Scanner(System.in);
        parrot myparrot = new parrot();

        System.out.println("What would you like to say to the parrot?");
        String text = input.nextLine();
        myparrot.speak(text);


    }
}
