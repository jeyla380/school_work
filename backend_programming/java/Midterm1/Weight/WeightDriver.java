/*
Jessemy Lake
CSIS 1400
 */

package Midterm1.Weight;

public class WeightDriver {

    public static void main(String[] args){

    Planet earth = new Planet("Earth", 9.78);
    Planet mars = new Planet("Mars", 3.71);

    String ename = earth.getPlanetName();
    double egravity = earth.getGravity();

    String mname = mars.getPlanetName();
    double mgravity = mars.getGravity();


    System.out.println("Planet Name       Gravity");
    System.out.printf("%s             %.02f\n",ename, egravity);
    System.out.printf("%s              %.02f\n", mname, mgravity);


    System.out.println();



    System.out.println("Weight for mass 22.49:");
    earth.calcWeight(22.49);
    mars.calcWeight(22.49);
    double emass = earth.getGravity();
    double mmass = mars.getGravity();
    System.out.printf("Earth: %.06f\n", emass);
    System.out.printf("Mars: %.06f\n", mmass);


    }
}
