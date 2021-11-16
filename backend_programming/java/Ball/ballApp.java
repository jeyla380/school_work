package Ball;

public class ballApp { //mainMethod

    public static void main(String[] args){

    ball myBall = new ball();

    myBall.setSize(5.0);
    double ballsize = myBall.getSize();


    int numberOfBounces = 1;

    System.out.printf("Size of ball: %.0f %n", ballsize);

        myBall.roll();
        myBall.bounce(numberOfBounces);


    ballsize = ++ballsize + 1;

    System.out.printf("New size of ball: %.0f", ballsize);



    }
}
