public class Team {

   private String name;
   private int wins;
   private int losses;
   
   //mutator methods
   public void setName(String setName)
   {
      name = setName;   
   }
   
   public void setWins(int setWins)
   {
      wins = setWins;   
   }
   
   public void setLosses(int setLosses)
   {
      losses = setLosses;   
   }
   
   //accessor methods
   public String getName()
   {
      return name;   
   }
   
   public int getWins()
   {
      return wins;   
   }
   
   public int getLosses()
   {
      return losses;   
   }
   
   public double getWinPercentage()
   {
      return (double) wins / (wins + losses);
   }
   
   public void printStanding()
   {
      System.out.printf("Win percentage: %.2f%n", getWinPercentage());
      if (getWinPercentage() >= 0.5)
      {
         System.out.printf("Congratulations, Team %s has a winning average!%n", name);   
      }
      else
      {
         System.out.printf("Team %s has a losing average.%n", name);   
      }
   }
   
}
