package Matrix;

public class MatrixMain {

    public static void main(String[] args){

        Matrix a = new Matrix(3, 4);
        Matrix b = new Matrix(3, 4);

        a.print();
        System.out.println();

        b.print();
        System.out.println();

        Matrix c = a.plus(b);
        c.print();
        System.out.println();

        Matrix d = new Matrix(c); //copy constructor
        d = d.plus(c);
        d.print();
        System.out.println();
    }
}
