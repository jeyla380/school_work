package Matrix;

import java.util.Random;

public class Matrix {
Random rand = new Random();

    private int n;
    private int m;
    private double[][] data;


    public Matrix(int n, int m){

        this.n = n;
        this.m = m;
        data = new double[n][m];

        Random rand = new Random();

        for(int i = 0; i < n; i++){

            for (int j = 0; j < m; j++){

                data[i][j] = rand.nextDouble();
            }
        }

        /*double[][] test1 = new double[m][n];

        for(int i = 0; i < m; i++){

            for(int j = 0; j < n; j++){

                test1[i][j] = rand.nextFloat();
            }
        }*/
    }


    public Matrix(Matrix a){
        n = a.n;
        m = a.m;
        data = new double[n][m];
//        data = a.data;
        //doesn't work

        for(int i = 0; i < n; i++){

            for(int j = 0; j < m; j++){

                data[i][j] = a.data[i][j];
            }
        }
    }

    public Matrix(double[][] a){

        n = a.length; //length of outside array (rows)
        m = a[0].length; //length of inside array (columns)
        data = a;
    }


    public Matrix plus(Matrix other){

        double [][] result = new double[n][m];

        for(int i = 0; i < n; i++){

            for(int j = 0; j < m; j++){

                result[i][j] = data[i][j] + other.data[i][j];
            }
        }
        return new Matrix(result);

        /*double[][] sumArray = new double[n][m];
        if(this.n == other.n && this.m == other.m){
            sumArray[i][j] = data[i][j] + other.data[i][j];
        }*/

    }

    public Matrix minus(Matrix other){

        return new Matrix(new double[1][1]);

        /*double[][] sumArray2 = new double[n][m];
        if(this.n == other.n && this.m == other.m){
            sumArray2[i][j] = data[i][j] - other.data[i][j];
        }*/
    }

    public void print(){
        for(int i = 0; i < n; i++){

            for(int j = 0; j < m; j++){

                System.out.printf("%4.2f ", data[i][j]);
            }
            System.out.println();
        }

    }

}
