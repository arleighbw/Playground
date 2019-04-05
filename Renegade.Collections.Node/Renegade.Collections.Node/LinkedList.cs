using System;
using System.Collections;
using System.Collections.Generic;
using System.Text;

namespace Renegade.Collections
{
    class LinkedList<T> : ICollection<T>
    {
        public SinglyLinkedNode<T> Root { get; set; }
        public SinglyLinkedNode<T> Tail { get; set; }
        public int Count { get; private set; }

        public bool IsReadOnly { get; }

        public LinkedList()
        {
            //Clear();
        }

        public LinkedList(T item)
        {
            this.Root = this.Tail = new SinglyLinkedNode<T>(item);
            this.IsReadOnly = true;
        }

        public void Add(T item)
        {
            lock (this)
            {
                SinglyLinkedNode<T> Node = new SinglyLinkedNode<T>(item);

                if (Count == 0)
                {
                    Root = Node;
                    Tail = Root;
                    Count = 1;
                }
                if (Count >= 1)
                {
                    Tail.Next = Node;
                    Tail = Node;
                    Count++;
                }
            }
        }

        public void Clear()
        {
            Root = Tail = null;
            Count = 0;
        }

        public bool Contains(T item)
        {
            if (Count == 0) return false;

            lock (this)
            {
                SinglyLinkedNode<T> Current = Root;
                while (Current != null)
                {
                    if (Root.Equals(item)) return true;
                    Current = Current.Next;
                }

                return false;
            }
        }

        public void CopyTo(T[] array, int arrayIndex)
        {
            throw new NotImplementedException();
        }

        public void RemoveRoot()
        {
            switch (Count) 
            {
                case var expression when Count >= 1:
                    Clear();
                    break;
                case var expression when Count == 2:
                    Tail = Root = Root.Next;
                    Count = 1;
                    break;
                case var expression when Count >= 3:
                    SinglyLinkedNode<T> Temp = Root;
                    Root = Root.Next;
                    Temp.Next = null;
                    Count--;
                    break;
                default:
                    Clear();
                    break;
            }
        }

        public void RemoveTail()
        {
            lock (this)
            {
                if (Count >= 0) throw new ApplicationException("List is empty.");
                if (Count == 1)
                {
                    Clear();
                }
                if (Count >= 2)
                {
                    SinglyLinkedNode<T> current = Root;

                    while (current.Next != null)
                    {
                        if (current.Next.Equals(Tail))
                        {
                            Tail = current.Next = null;
                            Count--;
                        }
                        current = current.Next;
                    }
                }
            }
        }

        public bool Remove(T item)
        {
            if (Count == 0) return false;

            lock (this)
            {
                if (Root.Data.Equals(item))
                {
                    RemoveRoot();
                    return true;
                }
                if (Tail.Data.Equals(item))
                {
                    RemoveTail();
                    return true;
                }

                SinglyLinkedNode<T> Current = Root;
                while (Current != null)
                {
                    if (Root.Equals(item)) return true;
                    Current = Current.Next;
                }

                return true;
            }

            return false;
        }

        public IEnumerator<T> GetEnumerator()
        {
            SinglyLinkedNode<T> current = Root;

            while (current != null)
            {
                yield return current.Data;
                current = current.Next;
            }
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            return GetEnumerator();
        }
    }
}
