
package DocComments;
/**
 * 
 * @author Jessemy
 */

public class TripPlanner {
    
    private String departure;
    private String arrival;
    private int distance;
    private Car car;
    
    /**
     * Constructor of class TripPlanner
     * 
     * @param departure city of departure
     * @param arrival city of arrival
     * @param distance distance between departure and arrival in miles
     * @param car make, model, and mpg of car
     */
    public TripPlanner(String departure, String arrival, int distance, Car car){
        this.departure = departure;
        this.arrival = arrival;
        this.distance = distance;
        this.car = car;
    }
    /**
     * returns the amount of fuel needed to make trip from departure to arrival
     * cities
     * @return fuelNeeded
     */
    public double fuelConsumption(){
        double fuelNeeded = (double)distance / (double)car.getMpg();
        return fuelNeeded;
    }

    @Override
    public String toString() {
        return "TripPlanner{" + "departure=" + departure + ", arrival=" + arrival + ", distance=" + distance + ", car=" + car.getModel() + '}';
    }
    
    
    
}
