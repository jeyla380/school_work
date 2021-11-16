/*
Jessemy Lake
CSIS 1400
Assignment 05
 */

package A05;

public class Triangle {

    private double side1;
    private double side2;
    private double side3;

    boolean yes = true;
    boolean no = false;


    private boolean isTriangle(double side1, double side2, double side3){


        double s1 = side1 * side1;
        double s2 = side2 * side2;
        double s3 = side3 * side3;


        if(side1 == 0 || side2 == 0 || side3 ==0){
            return no;
        }
        else if((s1 + s2 > s3) || (s1 + s3 > s2) || (s2 + s3 > s1)){
            return yes;
        }
        else if((s1 == s2) && (s1 == s3) && (s2 == s3)){
            return yes;
        }
        /*else if((s1 == s2) && (s2 != s3) || (s1 != s3)){
            return no;
        }*/
        return no;
    }


    public Triangle(double s1, double s2, double s3){

        if(isTriangle(s1, s2, s3)){
            side1 = s1;
            side2 = s2;
            side3 = s3;
        }
        else{
            side1 = 1;
            side2 = 1;
            side3 = 1;
        }

    }

    public double getSide1(){

        return side1;
    }

    public double getSide2(){

        return side2;
    }

    public double getSide3(){

        return side3;
    }

    public boolean isEquilateral(){

        double s1 = side1 * side1;
        double s2 = side2 * side2;
        double s3 = side3 * side3;

        if((s1 == s2) && (s1 == s3) && (s2 == s3)) {
            return yes;
        }
        else{
            return no;
        }

//        boolean isEquilateral = ((s1 == s2) && (s1 == s3)) ? yes : no;
//
//        return no;

    }

    public boolean isRight(){

        double s1 = side1 * side1;
        double s2 = side2 * side2;
        double s3 = side3 * side3;

        if((s1 + s2 == s3) || (s1 + s3 == s2) || (s2 + s3 == s1)){
            return yes;
        }
        else{
            return no;
        }

//        boolean isRight = ((s1 + s2 == s3) || (s1 + s3 == s2) || (s2 + s3 == s1)) ? yes : no;
//
//        return no;


    }



}
