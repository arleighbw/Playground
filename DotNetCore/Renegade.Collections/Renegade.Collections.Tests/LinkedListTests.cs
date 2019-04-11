using System;
using System.Text;
using Renegade.Collections;
using Xunit;

namespace Renegade.Collections.Tests
{
    public class LinkedListTests_String
    {
        [Fact]
        public void AddSingleNodeCount_Add_True()
        {
            var sLinkedList = new SinglyLinkedList<string>();

            sLinkedList.Add("Blayne");

            Assert.Equal(1, sLinkedList.Count);
        }

        [Fact]
        public void AddMultipleNodeCount_Add_True()
        {
            var sLinkedList = new SinglyLinkedList<string>();

            sLinkedList.Add("Blayne");
            sLinkedList.Add("Blayne2");
            sLinkedList.Add("Blayne3");

            Assert.Equal(3, sLinkedList.Count);
        }

        [Fact]
        public void AddMultipleNodeLinkedCorrectly_Add_True()
        {
            var sLinkedList = new SinglyLinkedList<string>();

            sLinkedList.Add("Blayne");
            sLinkedList.Add("Blayne2");
            sLinkedList.Add("Blayne3");
            sLinkedList.Add("Middle");
            sLinkedList.Add("Last");

            var sb = new StringBuilder();

            foreach (var node in sLinkedList)
            {
                sb.Append(node);
            }
            var actual = sb.ToString();
            
            Assert.Equal("BlayneBlayne2Blayne3MiddleLast", actual);
        }

        [Fact]
        public void ClearAllCountZero_Clear_True()
        {
            var sLinkedList = new SinglyLinkedList<string>();

            sLinkedList.Add("Blayne");
            sLinkedList.Add("Blayne2");
            sLinkedList.Add("Blayne3");
            sLinkedList.Clear();

            Assert.Equal(0, sLinkedList.Count);
        }

        [Fact]
        public void ClearAllCountRootNull_Clear_True()
        {
            var sLinkedList = new SinglyLinkedList<string>();

            sLinkedList.Add("Blayne");
            sLinkedList.Add("Blayne2");
            sLinkedList.Add("Blayne3");
            sLinkedList.Clear();

            Assert.Null(sLinkedList.Root);
        }

        [Fact]
        public void ClearAllCountTailNull_Clear_True()
        {
            var sLinkedList = new SinglyLinkedList<string>();

            sLinkedList.Add("Blayne");
            sLinkedList.Add("Blayne2");
            sLinkedList.Add("Blayne3");
            sLinkedList.Clear();

            Assert.Null(sLinkedList.Tail);
        }

        [Fact]
        public void ContainString_Contains_True()
        {
            var sLinkedList = new SinglyLinkedList<string>();

            sLinkedList.Add("Blayne");
            sLinkedList.Add("Blayne2");
            sLinkedList.Add("Blayne3");
            sLinkedList.Add("Middle");
            sLinkedList.Add("Last");

            Assert.True(sLinkedList.Contains("Middle"));
        }

        [Fact]
        public void DoesNotContainString_Contains_True()
        {
            var sLinkedList = new SinglyLinkedList<string>();

            sLinkedList.Add("Blayne");
            sLinkedList.Add("Blayne2");
            sLinkedList.Add("Blayne3");
            sLinkedList.Add("Middle");
            sLinkedList.Add("Last");

            Assert.False(sLinkedList.Contains("Yahoo"));
        }

        [Fact]
        public void EmptyList_Contains_True()
        {
            var sLinkedList = new SinglyLinkedList<string>();

            Assert.False(sLinkedList.Contains("Yahoo"));
        }
    }
}
