import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;

public class Arrays {

    /*
     * Complete the reverseArray function below.
     */
    static int[] reverseArray(int[] a) {
        int[] reversedArray = new int[a.length];
        
        for (int i = 0; i < a.length; i++) {
            reversedArray[i] = a[(a.length-1)-i];
        }
        
        return reversedArray;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int arrCount = Integer.parseInt(scanner.nextLine().trim());

        int[] arr = new int[arrCount];

        String[] arrItems = scanner.nextLine().split(" ");

        for (int arrItr = 0; arrItr < arrCount; arrItr++) {
            int arrItem = Integer.parseInt(arrItems[arrItr].trim());
            arr[arrItr] = arrItem;
        }

        int[] res = reverseArray(arr);

        for (int resItr = 0; resItr < res.length; resItr++) {
            bufferedWriter.write(String.valueOf(res[resItr]));

            if (resItr != res.length - 1) {
                bufferedWriter.write(" ");
            }
        }

        bufferedWriter.newLine();

        bufferedWriter.close();
    }
}

