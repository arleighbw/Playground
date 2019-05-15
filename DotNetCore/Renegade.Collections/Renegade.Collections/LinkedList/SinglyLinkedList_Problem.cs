using System;
using System.Collections.Generic;
using System.Text;

namespace Renegade.Collections
{
    public class SinglyLinkedList_Problem<T> : SinglyLinkedList<T>
    {
        /// <summary>
        /// Given a non-empty, singly linked list with head node head, return a middle node of linked list.
        ///
        ///If there are two middle nodes, return the second middle node.
        ///
        ///Example 1:
        ///
        ///Input: [1,2,3,4,5]
        ///Output: Node 3 from this list (Serialization: [3,4,5])
        ///The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
        ///Note that we returned a ListNode object ans, such that:
        ///ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
        ///Example 2:
        ///
        ///nput: [1,2,3,4,5,6]
        ///Output: Node 4 from this list (Serialization: [4,5,6])
        ///Since the list has two middle nodes with values 3 and 4, we return the second one.
        //Note:
        //The number of nodes in the given list will be between 1 and 100.
        /// <returns></returns>
        public T GetMiddleNode()
        {
            if (this.Root == null) return default(T);

            var curr = this.Root;
            var runner = this.Root;

            while (curr != null && runner?.Next != null)
            {
                curr = curr.Next;
                runner = runner.Next.Next;
            }

            return curr.Data;
        }

        /// <summary>
        /// Using a stack requires 2 passes.
        ///     Time Complexity O(2N)
        ///     Space Complexity O(N)
        /// </summary>
        /// <returns></returns>
        public bool IsPalindromeUsingStack()
        {
            if (Root == null) return false;

            var stack = new Stack<T>();

            var curr = this.Root;
            while (curr != null)
            {
                stack.Push(curr.Data);
                curr = curr.Next;
            }

            curr = this.Root;
            while (curr != null)
            {
                if (!curr.Data.Equals(stack.Pop())) return false;
                curr = curr.Next;
            }

            return true;
        }

        /// <summary>
        /// 
        /// </summary>
        /// <returns></returns>
        public bool IsCircular()
        {
            if (this.Root == null) return false;

            var curr = this.Root;
            var runner = this.Root;

            while (runner != null && runner.Next != null)
            {
                curr = curr.Next;
                runner = runner.Next.Next;

                if (curr == runner) return true;
            }

            return false;
        }
    }
}
