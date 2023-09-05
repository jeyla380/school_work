public class Artwork {
   
   private String title;
   private int yearCreated;
   
   private Artist artist;
   

   //default constructor
   public Artwork()
   {
      title = "unknown";
      yearCreated = -1;
      artist = new Artist();
   }
   
   //get methods
   public String getTitle()
   {
      return title;   
   }
   
   public int getYearCreated()
   {
      return yearCreated;   
   }

   //second constructor
   public Artwork(String title, int yearCreated, Artist artist)
   {
      this.title = title;
      this.yearCreated = yearCreated;
      this.artist = artist;
   }

   // TODO: Define printInfo() method
   //       Call the printInfo() method in Artist.java to print an artist's information 
   public void printInfo()
   {
      artist.printInfo();
      System.out.printf("Title: %s, %d%n", title, yearCreated);   
   }

}
