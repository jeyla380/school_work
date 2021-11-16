package LabPartyGuests;

import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

public class PartyGuests {

    public static void main(String[] args){

        int[] numberOfGuests = new int[4];
        Scanner input = new Scanner(System.in);
        Random rand = new Random();
        ArrayList<String> guestList = new ArrayList<>();


        System.out.println("Please enter 4 guests: ");

        for(int i = 1; i < 5; i++){
            System.out.printf("Guest %d: ", i);
            guestList.add(input.nextLine());

        }

        System.out.println();


        System.out.println("Guest List: " + guestList);


        String name = guestList.remove(rand.nextInt(4));
        System.out.println(name + " can't come");
        System.out.println("Updated Guest List: " + guestList);
    }
}
