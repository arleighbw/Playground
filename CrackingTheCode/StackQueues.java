import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class StackQueues {
    public static class MyQueue<T> {
        Stack<T> stackNewestOnTop = new Stack<T>();
        Stack<T> stackOldestOnTop = new Stack<T>();

        public void enqueue(T value) { // Push onto newest stack
            stackNewestOnTop.push(value);
        }

        public void moveToOldStack() {
            if (stackOldestOnTop.isEmpty()) {
                while (!stackNewestOnTop.isEmpty()) {
                    stackOldestOnTop.push(stackNewestOnTop.pop());
                }
            }    
        }
        
        public T peek() {
            moveToOldStack();
            
            return stackOldestOnTop.peek();
        }

        public T dequeue() {
            moveToOldStack();
            
            return stackOldestOnTop.pop();
        }
    }

    
    public static void main(String[] args) {
        MyQueue<Integer> queue = new MyQueue<Integer>();
        
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int x = 0;
        
        if (n > 0 && n <= 100000) {
            for (int i = 0; i < n; i++) {
                int operation = scan.nextInt();
                
                if (operation == 1) { // enqueue
                    x = scan.nextInt();
                    if (x > 0 && x <= 1000000000)
                    queue.enqueue(x);
                } else if (operation == 2) { // dequeue
                    queue.dequeue();
                } else if (operation == 3) { // print/peek
                    System.out.println(queue.peek());
                }
            }    
        }
        
        scan.close();
    }
}

