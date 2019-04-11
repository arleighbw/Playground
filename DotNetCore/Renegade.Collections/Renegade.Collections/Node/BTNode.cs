using System;
using System.Collections.Generic;
using System.Text;

namespace Renegade.Collections
{
    /// <summary>
    /// Node to be used in Binary Tree
    /// </summary>
    /// <typeparam name="T"></typeparam>
    public class BTNode<T> : Node<T>
    {
        public BTNode(T data) : base(data)
        {
        }

        public BTNode<T> Left { get; set; }
        public BTNode<T> Right { get; set; }
    }
}
