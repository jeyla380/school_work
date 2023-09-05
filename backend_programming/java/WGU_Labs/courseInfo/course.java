public class Course{
   private String courseNum;
   private String courseName;

   //set methods
   public void setCourseNumber(String courseNumber)
   {
      courseNum = courseNumber;   
   }
   
   public void setCourseTitle(String courseTitle)
   {
      courseName = courseTitle;   
   }


   //get methods
   public String getCourseNumber()
   {
      return courseNum;   
   }
   
   public String getCourseTitle()
   {
      return courseName;   
   }

   //print information
   public void printInfo()
   {
      System.out.println("Course Information:");
      System.out.printf("   Course Number: %s%n", courseNum);
      System.out.printf("   Course Title: %s%n", courseName);
   }
 
}
