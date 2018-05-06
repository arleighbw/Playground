import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class BalancedBrackets {
    
    public static boolean isBalanced(String expression) {
        Stack<Character> brackets = new Stack<Character>();
        
        for (char c: expression.toCharArray()) {
            if (c == '{') brackets.push('}');
            else if (c == '[') brackets.push(']');
            else if (c == '(') brackets.push(')');
            else {
                if (brackets.empty() || brackets.pop() != c) return false;
            }
        }
        
        return brackets.empty();
    }	
  
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for (int a0 = 0; a0 < t; a0++) {
            String expression = in.next();
            System.out.println( (isBalanced(expression)) ? "YES" : "NO" );
        }
    }
}


