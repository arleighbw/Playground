import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class AnagramCount {
    public static int numberNeeded(String first, String second) {
        int[] charCounts = new int[26];
        int result = 0;
        
        for (char c: first.toCharArray()) {
            charCounts[c - 'a']++;
        }
        
        for (char c: second.toCharArray()) {
            charCounts[c - 'a']--;
        }
        
        for (int count: charCounts) {
            result += Math.abs(count);
        }
        
        return result;
    }
  
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String a = in.next();
        String b = in.next();
        System.out.println(numberNeeded(a, b));
    }
}
