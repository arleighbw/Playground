using System;

class LinkedList { 
   
     static Node head; 
   
     public class Node { 
     
        public int data; 
        public Node next; 
   
        public Node(int d) { 
            data = d; 
            next = null; 
        } 
    } 
   
    /* Function to reverse the linked list */
    static Node reverse(Node node) { 
        Node prev = null; 
        Node current = node; 
        Node next = null; 
        while (current != null) { 
            next = current.next; 
            current.next = prev; 
            prev = current; 
            current = next; 
        } 
        
        return prev; 
    } 
   
    // prints content of double linked list 
    static void printList(Node node) { 
        while (node != null) { 
            Console.Write(node.data + " "); 
            node = node.next; 
        } 
    } 
   
    public static void Main(String []args) { 
        head = new Node(85); 
        head.next = new Node(15); 
        head.next.next = new Node(4); 
        head.next.next.next = new Node(20); 
           
        Console.WriteLine("Given Linked list"); 
        printList(head); 
        head = reverse(head); 
        Console.WriteLine(""); 
        Console.WriteLine("Reversed linked list "); 
        printList(head); 
    } 
}
