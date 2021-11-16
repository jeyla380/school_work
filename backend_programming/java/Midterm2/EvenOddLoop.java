package Midterm2;

public class EvenOddLoop {

    public static void main(String[] args){

        for(int i = 1; i < 10; i++){

            int j = i * i;
            if(j % 2 == 0){
                System.out.println(i + ": " + j + " is even");
            }
            else{
                System.out.println(i + ": " + j + " is odd");
            }

        }

    }
}
