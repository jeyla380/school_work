package Midterm2;

import java.util.Scanner;

public class AnimalSwitch {

    public static void main(String[] args){

        Scanner input = new Scanner(System.in);
        System.out.print("Please enter an animal (enter 'exit' to stop): ");
        String animal = input.nextLine();

        while(!animal.equalsIgnoreCase("Exit")){

            switch(animal){

                case "dog":
                    System.out.println("That's a mammal");
                    break;
                case "cat":
                    System.out.println("That's a mammal");
                    break;
                case "horse":
                    System.out.println("That's a mammal");
                    break;
                case "fish":
                    System.out.println("Lives in the water");
                    break;
                case "whale":
                    System.out.println("Lives in the water");
                    break;
                case "bird":
                    System.out.println("It can fly");
                    break;
                case "bat":
                    System.out.println("It can fly");
                    break;
                case "insect":
                    System.out.println("It can fly");
                    break;
                default:
                    System.out.println("Your choice: " + animal);
                    break;
            }
            System.out.print("Please enter an animal (enter 'exit' to stop): ");
            animal = input.nextLine();
        }

    }
}
