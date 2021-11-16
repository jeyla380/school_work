
package DocComments;


public class TravelApp {
    
    public static void main(String[] args){
        
        Car car1 = new Car("BMW", "M4", 25);
        System.out.printf("%s %s %d mpg.", car1.getMake(), car1.getModel(), car1.getMpg());
        System.out.println();
        
        Car car2 = new Car("Honda", "Civic", 42);
        System.out.printf("%s %s %d mpg.", car2.getMake(), car2.getModel(), car2.getMpg());
        System.out.println();
        System.out.println();
        
        TripPlanner trip1 = new TripPlanner("SF", "LA", 382, car1);
        System.out.println("California Trip: " + trip1.toString());
        System.out.printf("%.1f", trip1.fuelConsumption());
        System.out.println();
        
        TripPlanner trip2 = new TripPlanner("Tampa", "Miami", 280, car2);
        System.out.println("Florida Trip: " + trip2.toString());
        System.out.printf("%.1f", trip2.fuelConsumption());
        System.out.println();
    }
    
}
