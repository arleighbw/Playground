using System;

namespace Renegade.Collections
{
    /// <summary>
    /// Base class for Node to be used in DataStructures
    /// </summary>
    /// <typeparam name="T"></typeparam>
    public class Node<T> : IEquatable<T>
    {
        public T Data { get; set; }

        public Node(T data)
        {
            this.Data = data;
        }

        /// <summary>
        /// // IEquatable member to compare the data type of Node.
        /// </summary>
        /// <param name="other"></param>
        /// <returns></returns>
        public bool Equals(T other)
        {
            if (other == null) return false;
            return IEquatable<T>.Equals(this, other);
        }

        /// <summary>
        /// override of base class object.Equals to equate an equal node
        /// by if the Nodes Data Type Matches.
        /// </summary>
        /// <param name="obj"></param>
        /// <returns></returns>
        public override bool Equals(object obj)
        {
            if (obj == null) return false;

            Node<T> node = obj as Node<T>;

            return this.Data.Equals(node.Data);
        }

        /// <summary>
        /// Override currently doesn't do anything unique for this level.
        /// </summary>
        /// <returns></returns>
        public override int GetHashCode()
        {
            return base.GetHashCode();
        }

        /// <summary>
        /// Override this.Data.toString();
        /// </summary>
        /// <returns></returns>
        public override string ToString()
        {
            return this.Data.ToString();
        }
    }

}
