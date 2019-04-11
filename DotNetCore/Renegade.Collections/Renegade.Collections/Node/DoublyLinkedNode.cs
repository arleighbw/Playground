using System;
using System.Collections.Generic;
using System.Text;

namespace Renegade.Collections
{
    /// <summary>
    /// Node to be used in DoublyLinkedNode
    /// </summary>
    /// <typeparam name="T"></typeparam>
    public class DoublyLinkedNode<T> : Node<T>
    {
        public DoublyLinkedNode(T data) : base(data)
        {
        }

        public DoublyLinkedNode<T> Next { get; set; }
        public DoublyLinkedNode<T> Prev { get; set; }
    }
}
