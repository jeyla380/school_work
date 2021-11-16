/*
Jessemy Lake
CSIS 1400
 */

package Midterm1.Weight;

public class Planet {

    private String planetName;
    private double gravity;

    public Planet(String pn, double g){

        planetName = pn;
        gravity = g;
    }

    public String getPlanetName(){

        return planetName;
    }

    public double getGravity(){

        return gravity;
    }

    public void calcWeight(double m){

        gravity = (gravity * m);
    }
}
