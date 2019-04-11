using System;
using System.Collections.Generic;
using System.Text;

namespace Renegade.Collections
{
    /// <summary>
    /// Node to be used in SinglyLinkedList
    /// </summary>
    /// <typeparam name="T"></typeparam>
    public class SinglyLinkedNode<T> : Node<T>
    {
        public SinglyLinkedNode(T data) : base(data)
        {
        }

        public SinglyLinkedNode<T> Next { get; set; }
    }
}
