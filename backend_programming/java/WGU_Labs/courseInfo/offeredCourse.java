public class OfferedCourse extends Course {
   private String instructorName;
   private String classLocation;
   private String classTime;

   //set/mutator methods
   public void setInstructorName(String iName)
   {
      instructorName = iName;   
   }
   
   public void setLocation(String location)
   {
      classLocation = location;   
   }
   
   public void setClassTime(String time)
   {
      classTime = time;
   }


   //get/accessor methods
   public String getInstructorName()
   {
      return instructorName;   
   }
   
   public String getLocation()
   {
      return classLocation;   
   }
   
   public String getClassTime()
   {
      return classTime;   
   }

}
