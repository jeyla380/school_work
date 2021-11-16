/*
Jessemy Lake
CSIS 1400
 */



package Midterm1;

import java.util.Scanner;

public class Score {

    public static void main(String[] args){

        Scanner input = new Scanner(System.in);

        System.out.println("Enter the name of the first team: ");
        String team1 = input.nextLine();

        System.out.println("Enter the first team's score: ");
        int score1 = input.nextInt();


        System.out.println("Enter the name of the second team: ");
        String team2 = input.next();

        System.out.println("Enter the second team's score: ");
        int score2 = input.nextInt();


        if(score1 > score2){
            System.out.printf("%s is the winner!", team1);
        }

        if(score2 > score1){
            System.out.printf("%s is the winner!", team2);
        }

    }
}
