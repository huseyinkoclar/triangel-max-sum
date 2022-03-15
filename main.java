import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.Scanner;

class main{
    static int [][] lines = new int[6][6];
    static int [] results = new int[99];
    static int counter = 0;
    public static void main(String args[]) throws FileNotFoundException{
        Scanner sc = new Scanner(new BufferedReader(new FileReader("input1.txt")));
        

        while(sc.hasNextLine()) {
            for (int i=0; i<lines.length; i++) {
               String[] line = sc.nextLine().trim().split(" ");
               for (int j=0; j<line.length; j++) {
                  lines[i][j] = Integer.parseInt(line[j]);
               }
            }
         }
        
        //lines = cleanArr(lines);

        System.out.println(sum(0,0,0));
        
        twoDimensionalPrinting();
    }


    static int sum(int total, int i, int j){


        if ( i != lines.length){
            return total += lines[i][j] + sum(total,i+1,j);
        }
        else {results[counter] = total; counter++; return total;}

    }


    static boolean isPrime(int n)
    {
        if (n <= 1)
            return false;
        for (int i = 2; i < n; i++)
            if (n % i == 0)
                return false;
        return true;
    }


    //need to optimized for not turning ZEROS
    static int [][] cleanArr(int[][] arr){
        for ( int[] line : lines){
            for(int i = 0; i<line.length;i++)
                if(isPrime(line[i]))
                    line[i] = 0;
        }
        return lines;


    }


    //two dimensional array printing
    static void twoDimensionalPrinting(){
        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 6; j++) {
                System.out.print(lines[i][j] + " ");
            }
            System.out.println();
        }
    }


}