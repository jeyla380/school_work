
package DocComments;
/**
 * Make, model, and miles per gallon of a car
 * 
 * @author Jessemy
 */

public class Car {
    
    private String make;
    private String model;
    private int mpg;
    
    /**
     * 
     * @param make the make of a car
     * @param model the model of car
     * @param mpg the miles per gallon of a car
     */
    public Car(String make, String model, int mpg){
        this.make = make;
        this.model = model;
        this.mpg = mpg;
    }
    /**
     * returns the make of a car
     * @return make
     */
    public String getMake(){
        return make;
    }
    /**
     * returns the model of a car
     * @return model
     */
    public String getModel(){
        return model;
    }
    /**
     * returns the miles of gallon of a car
     * @return mpg
     */
    public int getMpg(){
        return mpg;
    }
    
}
