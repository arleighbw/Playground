/*
Detect a cycle in a linked list. Note that the head pointer may be 'null' if the list is empty.

A Node is defined as: 
    class Node {
        int data;
        Node next;
    }
*/

public boolean hasCycle(Node head) {
    if (head == null) return false;
    
    Node slow = head;
    Node fast = head;
    
    while (fast != null && fast.next !=null) {
        fast = fast.next.next;
        slow = slow.next;
        
        if (slow == fast) return true;
    }
    
    return false;
}

