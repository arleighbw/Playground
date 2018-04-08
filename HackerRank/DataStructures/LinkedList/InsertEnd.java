/*
  Insert Node at the end of a linked list 
  head pointer input could be NULL as well for empty list
  Node is defined as 
  class Node {
     int data;
     Node next;
  }
*/
Node Insert(Node head,int data) {
// This is a "method-only" submission. 
// You only need to complete this method.
    Node current = head;
    
    while (current.next != null) {
        current = current.next;
    }
    
    Node tail = new Node();
    tail.data = data;
    tail.next = null;
    current.next = tail;
    return head;
}

