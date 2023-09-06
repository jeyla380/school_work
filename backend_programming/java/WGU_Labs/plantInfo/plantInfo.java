import java.util.Scanner;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class PlantArrayListExample {

   public static void printArrayList(ArrayList<Plant> plantObjects)
   {
      for (int j = 0; j < plantObjects.size(); j++)
      {  
         int k = j + 1;
         if (j == plantObjects.size() - 1)
         {
            System.out.printf("Plant %d Information:%n", k);
            plantObjects.get(j).printInfo();   
         }
         else
         {
            System.out.printf("Plant %d Information:%n", k);
            plantObjects.get(j).printInfo();
            System.out.println();
         }
      }
   }
   
   public static void main(String[] args) {
      Scanner scnr = new Scanner(System.in);
      String input;
      ArrayList<Plant> myGarden = new ArrayList<Plant>();

      String plantName;
      int plantCost;
      String flowerName;
      int flowerCost;
      String colorOfFlowers;
      boolean isAnnual;
      
      int i = 1;
      while (i > 0)
      {
         input = scnr.nextLine();
         if (input.equals("-1"))
         {
            i = 0;   
         }
         else
         {
            //System.out.println(input);
            String[] inputString = input.split(" ", 5);
            //for (String x : inputString)
               //System.out.println(x);
            if (inputString[0].equals("plant"))
            {
               Plant myPlant = new Plant();
               myPlant.setPlantName(inputString[1]);
               myPlant.setPlantCost(inputString[2]);
               
               myGarden.add(myPlant);
            }
            else if (inputString[0].equals("flower"))
            {
               Flower myFlower = new Flower();
               myFlower.setPlantName(inputString[1]);
               myFlower.setPlantCost(inputString[2]);
               myFlower.setPlantType(Boolean.parseBoolean(inputString[3]));
               myFlower.setColorOfFlowers(inputString[4]);
               
               myGarden.add(myFlower);
            }
         }
      }
      
      printArrayList(myGarden);
   }
}
