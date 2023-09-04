import java.util.Scanner;

public class TriangleArea {
   public static void main(String[] args) {
      Scanner scnr = new Scanner(System.in);
      
      Triangle triangle1 = new Triangle();
      Triangle triangle2 = new Triangle();

      // TODO: Read and set base and height for triangle1 (use setBase() and setHeight())
      triangle1.setBase(scnr.nextDouble());
      triangle1.setHeight(scnr.nextDouble());
      
      // TODO: Read and set base and height for triangle2 (use setBase() and setHeight())
      triangle2.setBase(scnr.nextDouble());
      triangle2.setHeight(scnr.nextDouble());
      
      
      System.out.println("Triangle with smaller area:");
      
      // TODO: Determine smaller triangle (use getArea())
      //       and output smaller triangle's info (use printInfo())
      if (triangle1.getArea() < triangle2.getArea())
      {
         triangle1.printInfo();   
      }
      else
      {
         triangle2.printInfo();   
      }
      
   }
}
