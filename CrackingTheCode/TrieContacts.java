import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class TrieContacts {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        
        TrieTree contactTree = new TrieTree(); 
        
        for(int a0 = 0; a0 < n; a0++){
            String op = in.next();
            String contact = in.next();
            
            if (op.equals("add")) {
                contactTree.add(contact);
            }
            if (op.equals("find")) {
                System.out.println(contactTree.findPartialCount(contact));
            }
        }
    }
}

class TrieTree {
    private Node root;
    
    public TrieTree() {
        root = new Node('*');
    }
    
    public void add(String addContact) {
    	Node curr = root;
    	
    	for (char c: addContact.toCharArray()) {
    		curr.add(c);	
    		curr = curr.findChildNode(c);
    		curr.count++;                             // increments either way !!
    	}
    }
    
    public int findPartialCount(String findContact) {
    	Node curr = root;
    	
    	for (char c: findContact.toCharArray()) {
    		curr = curr.findChildNode(c);
    		if (curr==null) return 0;
    	}
    	
    	return curr.count;
    }
}

class Node {
    
    private char letter;
    private HashMap<Character,Node> children = new HashMap<Character,Node>();
    public int count;
    
    public Node(char letter) {
        this.letter = letter;
    }
    
    public void add(char c) {
    	children.putIfAbsent(c, new Node(c));
    }
    
    public Node findChildNode(char c) {
    	return children.get(c);
    }
}
