/**********************************************
* Author: Jessemy Lake
* 
* RobotApp solved three challenges where a 
* robot needs to figure out the number
* of rooms in a given grid.
*
* Important: 
* The code still needs to work when you change
* the values of the variables n, h, and w.
***********************************************/
package A06;

public class RobotApp {
	public static void main(String[] args) {
      
      int n = 5;
      int h = 4;
      int w = 6;
      
      // square nxn grid with the robot in the north-east corner
      Robot robot = new Robot(n, n, n-1, 0);
      challenge1(robot);    
      
      // rectangular grid with width w and height h
      // robot in the north-east corner
      robot = new Robot(w, h, w-1, 0);  
      challenge2(robot);
      
      // square nxn grid 
      // robot's starting position: 1 over, 2 down 
      robot = new Robot(n, n, 1, 2);   
      challenge3(robot);      
      
      // rectangular grid with width w and height h
      // robot's starting position: 3 over, 1 down 
      robot = new Robot(w, h, 3, 1);   
      challenge4(robot);
	}
     
   private static void challenge1(Robot robot) {      
      // TODO: Solve challenge 1 and update the text below
       int x = 1;

       while(robot.check('S')){
           robot.go('S');
           x++;
       }

       int n = x - 1;
       x = x * x;

      robot.say(x + " rooms " + n + " moves");
   }
   
   private static void challenge2(Robot robot) {      
      // TODO: Solve challenge 2 and update text below
       int y = 1;

       while(robot.check('S')){
           robot.go('S');
           y++;
       }
       int x = 1;
       while(robot.check('W')){
           robot.go('W');
           x++;
       }
       int h = y - 1;

       int w = x - 1;

       int totalMoves = w + h;
       int totalRooms = (x * y);
   
      robot.say(totalRooms + " rooms " + totalMoves + " moves");
   }
   
   private static void challenge3(Robot robot) {   
      // TODO: Solve challenge 3 and update text below
       int m = 1;
       while(robot.check('W')){
           robot.go('W') ;
           m++;
       }
       int x = 1;
       while(robot.check('E')){
           robot.go('E') ;
           x++;
       }

       int n = (m + x) - m; //correct
       x = x * n;

       //while(robot.check('N) || (robot.check('E');
   
      robot.say( x + " rooms " + n + " moves");
   }
      
   private static void challenge4(Robot robot) {   
      // TODO: Solve challenge 4 and update text below
       int m = 1;
       while(robot.check('N')){
           robot.go('N') ;
           m++;
       }
       int y = 1;
       while(robot.check('S')){
           robot.go('S') ;
           y++;
       }

       int t = (m + y) - m; //correct
       y = y * t;

       int o = 1;
       while(robot.check('E')){
           robot.go('E') ;
           o++;
       }
       int x = 1;
       while(robot.check('W')){
           robot.go('W') ;
           x++;
       }

       int s = (o + x) - o;
       x = x * s;

       int u = s + t;
       int z = (x - y) + t;
   
      robot.say(z + " rooms " + u + " moves");
   }

/*   // This method briefly demonstrates how the robot
   // can be controlled.
   private static void demo(Robot robot) {
		int x = 3;
		robot.go('S');
      robot.go('W');
		if (robot.check('N')) {
			robot.go('N');
         x++;
		}
		robot.go('E');
      // robot.go('E'); // uncomment this line and see what happens

		robot.say( x + " rooms 2n + 5 moves");
   }*/
}
