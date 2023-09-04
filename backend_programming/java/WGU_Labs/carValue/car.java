public class Car {
   private int modelYear; 
   private int purchasePrice;
   private int currentValue;
   
   public void setModelYear(int userYear){
      modelYear = userYear;
   }
   
   public int getModelYear() {
      return modelYear;
   }
   
   public void setPurchasePrice(int userPrice)
   {
      purchasePrice = userPrice;   
   }
   
   public int getPurchasePrice()
   {
      return purchasePrice;   
   }
   
   
   public void calcCurrentValue(int currentYear) {
      double depreciationRate = 0.15;
      int carAge = currentYear - modelYear;
      
      // Car depreciation formula
      currentValue = (int) 
         Math.round(purchasePrice * Math.pow((1 - depreciationRate), carAge));
   }
   
   public void printInfo()
   {
      System.out.println("Car's information:");
      System.out.printf("  Model year: %d%n", modelYear);
      System.out.printf("  Purchase price: $%d%n", purchasePrice);
      System.out.printf("  Current value: $%d%n", currentValue);
   }
   
}
