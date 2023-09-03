import java.util.Scanner;

public class LabProgram {

   public static void sortArray(int[] myArr, int arrSize)
   {  
      //selection sort
      int temp = 0;
      for (int i = 0; i < arrSize; i++)
      {
         //find the max element
         int maxIndex = i;
         for (int j = i + 1; j < arrSize; j++)
         {
            if (myArr[j] > myArr[maxIndex])
            {
               maxIndex = j;   
            }
         }
         
         temp = myArr[maxIndex];
         myArr[maxIndex] = myArr[i];
         myArr[i] = temp;
         
         if (myArr[i] == myArr[myArr.length - 1])
         {
            System.out.printf("%d,%n", myArr[i]);  
         }
         else
         {
            System.out.printf("%d,", myArr[i]);
         }
      }
   }

  
   public static void main(String[] args) {
      Scanner scnr = new Scanner(System.in);
      int inputNum = scnr.nextInt();
      int[] numArr = new int[inputNum];
      
      for (int k = 0; k < inputNum; k++)
      {
         numArr[k] = scnr.nextInt(); 
      }
      sortArray(numArr, inputNum);
   }
}
